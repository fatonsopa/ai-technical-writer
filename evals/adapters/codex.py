"""Bounded Codex CLI transport; no task rubric or acceptance decisions."""
import datetime
import json
import os
import re
import signal
import subprocess
import time

def invoke(work, output, prompt, model, schema_value, budget, grading=False):
    output.mkdir(parents=True, exist_ok=True)
    schema_path = output / 'schema.json'
    schema_path.write_text(json.dumps(schema_value))
    last = output / 'response.json'
    cmd = ['codex', 'exec', '--ignore-user-config', '--ephemeral', '--skip-git-repo-check',
           '--sandbox', 'read-only', '--model', model, '--json', '--output-schema', str(schema_path),
           '-C', str(work), '-o', str(last), '-']
    started = time.monotonic()
    record = {'model': model, 'command_options': cmd[2:11], 'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    process_started = False
    try:
        if budget is None:
            raise ValueError('Configure maximum CLI invocations and total runtime before live evaluation.')
        timeout = budget.reserve()
        with (output / 'events.jsonl').open('w') as events, (output / 'stderr.txt').open('w') as errors:
            process = subprocess.Popen(cmd, stdin=subprocess.PIPE, text=True, stdout=events, stderr=errors, start_new_session=True)
            process_started = True
            try:
                process.communicate(prompt, timeout=timeout)
            except subprocess.TimeoutExpired:
                try: os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError: pass
                process.communicate()
                raise
            result = process
        if result.returncode:
            raise RuntimeError('Codex exited ' + str(result.returncode) + '; inspect local stderr')
        data = json.loads(last.read_text())
        if not isinstance(data.get('results'), list): raise ValueError('Response needs a results array.')
        usage = []; commands = []
        for line in (output / 'events.jsonl').read_text().splitlines():
            event = json.loads(line)
            if event.get('type') == 'turn.completed': usage.append(event.get('usage', {}))
            item = event.get('item', {})
            if event.get('type') == 'item.completed' and item.get('type') == 'command_execution':
                commands.append(item.get('command', ''))
        record.update(status='completed', results=data['results'], usage=usage,
                      references_in_commands=sorted(set(re.findall(r'references/[a-z_\-]+\.md', '\n'.join(commands)))),
                      runtime_resources_in_commands=sorted(set(re.findall(r'(?:references|examples|workflows)/[a-z_\-]+\.md', '\n'.join(commands)))))
    except (subprocess.TimeoutExpired, RuntimeError, ValueError, OSError, KeyError, TypeError) as error:
        record.update(status='infrastructure_error', error=str(error))
        if process_started and not grading and isinstance(error, (ValueError, KeyError, TypeError)):
            record['error_kind'] = 'task_output'
    record['elapsed_seconds'] = round(time.monotonic() - started, 2)
    if budget is not None: record['budget'] = budget.report()
    (output / 'record.json').write_text(json.dumps(record, indent=2) + '\n')
    return record

