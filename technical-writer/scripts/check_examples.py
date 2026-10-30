#!/usr/bin/env python3
"""Exercise the authored local Python examples in disposable directories."""
import importlib.util
import json
from pathlib import Path
import shlex
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('validator', HERE / 'validate_skill.py')
validator = importlib.util.module_from_spec(spec); spec.loader.exec_module(validator)


def example(name):
    docs = [body for tag, body in validator.blocks((HERE.parent / 'references' / name).read_text())[0] if tag == 'md']
    return docs[-1]


def execute(command, cwd):
    args = shlex.split(command)
    if not (args[:2] == ['python3', '-c'] or args[0] == 'cp'): raise ValueError('Unexpected example command')
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=True, timeout=15)
    return result.stdout.strip()


def check():
    results = []
    with tempfile.TemporaryDirectory(prefix='writer-example-') as directory:
        cwd = Path(directory)
        blocks = validator.blocks(example('tutorial.md'))[0]
        (cwd / 'settings.json').write_text(next(body for tag, body in blocks if tag == 'json'))
        outputs = [execute(body, cwd) for tag, body in blocks if tag == 'sh']
        assert outputs == ['Example App'], outputs
        results.append('tutorial: JSON input and expected output verified')
    with tempfile.TemporaryDirectory(prefix='writer-example-') as directory:
        cwd = Path(directory); blocks = validator.blocks(example('how_to_guide.md'))[0]
        (cwd / 'settings.json').write_text(next(body for tag, body in blocks if tag == 'json'))
        commands = [body for tag, body in blocks if tag == 'sh']
        outputs = [execute(body, cwd) for body in commands[:3]]
        assert outputs[-1] == 'Port updated'
        assert json.loads((cwd / 'settings.json').read_text()) == {'port':3100, 'debug':False}
        execute(commands[3], cwd)
        assert json.loads((cwd / 'settings.json').read_text()) == {'port':3000, 'debug':False}
        results.append('how-to: backup, isolated edit, preservation, check, and recovery verified')
    with tempfile.TemporaryDirectory(prefix='writer-example-') as directory:
        cwd = Path(directory); (cwd / 'tests').mkdir()
        (cwd / 'sample.json').write_text('{"project":"Example App"}')
        (cwd / 'report.py').write_text('import json,sys\nprint(json.load(open(sys.argv[1]))["project"])\n')
        (cwd / 'tests/test_report.py').write_text('import subprocess,unittest\nclass Report(unittest.TestCase):\n def test_name(self):\n  self.assertEqual(subprocess.check_output(["python3","report.py","sample.json"],text=True).strip(),"Example App")\n')
        start = subprocess.run(['python3','report.py','sample.json'],cwd=cwd,capture_output=True,text=True,check=True)
        assert start.stdout.strip() == 'Example App'
        subprocess.run(['python3','-m','unittest','discover','-s','tests'],cwd=cwd,capture_output=True,text=True,check=True)
        results.append('README: commands verified against the explicitly stated fictional repository contract')
    return results


if __name__ == '__main__':
    print(json.dumps({'passed':check(),'limits':'These local examples do not test a real application, host activation, production system, or every generated command.'},indent=2))
