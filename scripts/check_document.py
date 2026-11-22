#!/usr/bin/env python3
"""Check the requested structure of a draft; source and language still need review."""
import argparse
import json
from pathlib import Path

from document_contracts import validate, load_contracts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('document', type=Path)
    parser.add_argument('--kind', required=True, choices=sorted(load_contracts()['documents']))
    parser.add_argument('--operation', choices=['create', 'rewrite', 'edit', 'review'], default='create')
    parser.add_argument('--scope', choices=['complete', 'excerpt', 'title'], default='complete')
    parser.add_argument('--context', type=Path, help='Optional declared document context JSON.')
    args = parser.parse_args()
    try:
        context = json.loads(args.context.read_text()) if args.context else None
        for declared in [(context or {}).get('coverage'), *(context or {}).get('parents', [])]:
            if declared and 'path' in declared:
                source = (args.context.parent / declared['path']).resolve()
                declared.setdefault('source', declared['path'])
                declared['source_text'] = source.read_text() if source.is_file() else None
        result = validate(args.document.read_text(), args.kind, args.operation, args.scope, context=context)
        print(json.dumps(result, indent=2))
        return 0 if result['passed'] else 1
    except (ValueError, OSError, TypeError) as error:
        print(json.dumps({'passed': False, 'findings': [str(error)], 'semantic_review_required': True}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
