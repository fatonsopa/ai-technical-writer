#!/usr/bin/env python3
"""Regression checks for the advisory language scanner."""
from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("plain_words", HERE / "plain_words.py")
pw = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(pw)


def test_scanner():
    sample = """# Heading
In order to improve results, the system provides visibility into tasks.
```bash
leverage --help
```
Use `leverage` as a literal command and read https://example.com/seamless.
The service is robust.
"""
    suggestions = pw.findings(sample)
    phrases = [phrase.lower() for _, phrase, _ in suggestions]
    assert "in order to" in phrases
    assert "provides visibility into" in phrases
    assert "robust" in phrases
    assert "leverage" not in phrases
    assert "seamless" not in phrases
    assert all(number in (2, 7) for number, _, _ in suggestions)

    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "document.md"
        p.write_text(sample)
        assert pw.main([str(p)]) == 0, "advice must not block by default"
        assert pw.main(["--strict", str(p)]) == 1, "strict mode can fail"
        assert pw.main(["--strict", "--report", str(p)]) == 0
        assert pw.main(["--anchors", str(p)]) == 0


if __name__ == "__main__":
    test_scanner()
    print("plain_words tests passed")
