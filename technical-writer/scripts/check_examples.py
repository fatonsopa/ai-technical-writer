#!/usr/bin/env python3
"""Execute the offline teaching exercise; never run the source application."""
import importlib.util
import json
from pathlib import Path
import shlex
import subprocess
import tempfile
import textwrap

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('validator', HERE / 'validate_skill.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def check():
    example = HERE.parent / 'examples/tutorial.md'
    blocks, broken = validator.blocks(example.read_text())
    assert not broken
    fixture = next(body for tag, body in blocks if tag == 'json')
    commands = [body for tag, body in blocks if tag == 'sh']
    expected = [body for tag, body in blocks if tag == 'text']
    assert len(commands) == len(expected) == 2
    with tempfile.TemporaryDirectory(prefix='writer-example-') as directory:
        work = Path(directory)
        (work / 'websites.json').write_text(fixture)
        for command, output in zip(commands, expected):
            args = shlex.split(command)
            assert args[:2] == ['python3', '-c']
            result = subprocess.run(args, cwd=work, capture_output=True, text=True, check=True, timeout=15)
            assert result.stdout.strip() == textwrap.dedent(output).strip(), result.stdout
        readme_blocks = validator.blocks((HERE.parent / 'examples/readme.md').read_text())[0]
        readme_command = next(body for tag, body in readme_blocks if tag == 'sh')
        args = shlex.split(readme_command)
        assert args[:2] == ['python3', '-c']
        result = subprocess.run(args, cwd=work, capture_output=True, text=True, check=True, timeout=15)
        assert result.stdout.strip() == 'U3, U3H, US'
        rows = json.loads(fixture)
        assert len(rows) == 9
        assert next(row for row in rows if row['id'] == 'U3H')['cited'] is False
        assert next(row for row in rows if row['id'] == 'UD')['active'] is False
    return ['Tutorial commands match both displayed outputs in a clean temporary directory',
            'README first command matches its documented output',
            'Nine-state fixture retains the uncited Review row and deleted-row distinction']


if __name__ == '__main__':
    print(json.dumps({'passed': check(), 'limits': 'Offline Python teaching exercise only. Application, UI how-to, SQL, actual reports, and host activation are not executed by this check.'}, indent=2))
