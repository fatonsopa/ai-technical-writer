#!/usr/bin/env python3
"""Compatibility entry point; shared diagram rendering lives in render_diagram."""
import sys
import render_diagram

if __name__ == "__main__":
    raise SystemExit(render_diagram.main())
sys.modules[__name__] = render_diagram
