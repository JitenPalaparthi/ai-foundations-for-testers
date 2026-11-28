"""Run every selected standalone example; preserve failures in the exit code."""
import argparse
from pathlib import Path
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["sync", "async", "both"], default="both")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--chrome", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    modes = ["sync", "async"] if args.mode == "both" else [args.mode]
    results = []
    for mode in modes:
        for script in sorted((root / mode).glob("[0-9]*.py")):
            command = [sys.executable, str(script)]
            if args.headless:
                command.append("--headless")
            if args.chrome:
                command.append("--chrome")
            print(f"\nRUN: {mode}/{script.name}", flush=True)
            try:
                result = subprocess.run(command, cwd=root, timeout=120)
                passed = result.returncode == 0
            except subprocess.TimeoutExpired:
                print("FAIL: example exceeded 120 seconds", flush=True)
                passed = False
            results.append((f"{mode}/{script.name}", passed))
    print("\nRESULTS", flush=True)
    for name, passed in results:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    failed = sum(not passed for _, passed in results)
    print(f"{len(results) - failed} passed; {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
