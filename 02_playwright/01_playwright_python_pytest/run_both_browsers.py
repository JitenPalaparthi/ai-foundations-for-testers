"""Run all selected examples on Chromium and Firefox using the current Python.

Examples:
    python run_both_browsers.py -v
    python run_both_browsers.py test_01_first_test.py --headed -v
    python run_both_browsers.py --run-public -v
    python run_both_browsers.py --collect-only -q

Other pytest options are forwarded. Public examples remain opt-in.
"""
from pathlib import Path
import subprocess
import sys


def main():
    arguments = sys.argv[1:]
    for argument in arguments:
        if argument.split("=", 1)[0] in {"--browser", "--browser-channel", "--device"}:
            print("This runner uses Chromium and Firefox without a device override. "
                  "Use python -m pytest directly for another browser configuration.", file=sys.stderr)
            return 2
    command = [sys.executable, "-m", "pytest", "--browser", "chromium",
               "--browser", "firefox", *arguments]
    return subprocess.run(command, cwd=Path(__file__).resolve().parent).returncode


if __name__ == "__main__":
    raise SystemExit(main())
