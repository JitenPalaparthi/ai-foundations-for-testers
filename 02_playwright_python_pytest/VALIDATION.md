# Chromium and Firefox validation status

Checked on 19 November 2026 with Python 3.9.6 on macOS. Use Python 3.10+ for a fresh workshop installation.

Top-level packages: Playwright 1.60.0, pytest-playwright 0.7.1, pytest 8.4.2, pytest-html 4.2.0, pytest-xdist 3.8.0. Exact versions are in requirements-validated.txt.

## Compatibility changes

- Every browser example now includes an explicit Chromium + Firefox run command.
- run_both_browsers.py selects both engines and forwards test selection/reporting options to pytest. It preserves pytest's exit code.
- Example 24 uses pytest-playwright's new_context fixture so restored storage is tested in the selected engine with fixture-managed lifecycle/artifacts.
- Example 29 and its exercise use viewport dimensions on both engines. The previous Chromium-only iPhone exercise was removed. Firefox does not support full mobile emulation.
- No browser-specific skip or only-browser marker hides an example from either engine. Only the two optional public-site examples are skipped by default, on both engines.

## Checks completed

- All Python files parse successfully.
- The dual-browser runner was executed from outside the bundle to verify that it finds its test directory.
- Collection contains 75 cases: 37 Chromium cases, the matching 37 Firefox cases, and 1 browser-independent API case. The paired browser case IDs were checked for exact coverage parity.
- By default, the 4 public browser cases are skipped, leaving 71 local executions. Enabling --run-public selects all 75.
- The direct API example passed through the dual-browser runner and generated an HTML report and JUnit XML. validation/api-report.html and api-results.xml represent this API example only.
- Prior site checks verified HTTP 200 for the local page, iframe, help page, download, and users API; unique HTML IDs and valid label targets; and inline JavaScript syntax.
- The public TodoMVC source was inspected previously to confirm its test-ID and Delete button selectors. Public browser interactions have not been executed.

Collection details are in validation/collected-tests.txt. Machine-readable status is in validation/cross-browser-status.json.

## Browser execution limitation — no full-suite pass claimed

The matching Chromium headless shell (build 1223) and Firefox (build 1522) were installed. Example 01 was then attempted on both engines:

| Engine | Observed result |
|---|---|
| Chromium | Startup fails before the test opens a page. macOS reports MachPortRendezvousServer registration permission denied (1100). |
| Firefox | Startup fails before the test opens a page. The process aborts with SIGABRT; its log does not establish the root cause. |

The earlier headed Chromium attempt also failed at startup. This session therefore cannot certify that browser test bodies pass on either engine. Trace/video capture, Inspector interaction, and parallel browser execution remain unverified. Expected outcomes in teaching notes are instructional expectations, not recorded full-suite results. Public sites also depend on internet availability and their current DOM.

## Run from your terminal before class

```sh
python -m pip install -r requirements.txt
python -m playwright install chromium firefox
python run_both_browsers.py -v
python run_both_browsers.py test_01_first_test.py --headed --slowmo 350 -v
python run_both_browsers.py --tracing retain-on-failure --screenshot only-on-failure --html=reports/both-browsers.html --self-contained-html --junitxml=reports/both-browsers.xml -v
```

A successful default run should report 71 passed and 4 skipped. To include public examples, use `python run_both_browsers.py --run-public -v`; a successful run then reports 75 passed. For one engine at a time, use `python -m pytest --browser chromium -v` and `python -m pytest --browser firefox -v`. See COMMANDS.md for all commands.

References: [browser installation and multiple engines](https://playwright.dev/python/docs/browsers), [pytest fixture and CLI reference](https://playwright.dev/python/docs/test-runners).
