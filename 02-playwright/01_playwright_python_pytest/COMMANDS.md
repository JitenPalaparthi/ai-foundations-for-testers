# All workshop commands

Run from this bundle directory with the virtual environment active. Use `python3` only for environment creation on macOS/Linux, then `python` after activation. Windows uses `py` to create the environment. Installation instructions for both platforms are in README.md.

## Run both requested browsers

```sh
python -m playwright install chromium firefox
python run_both_browsers.py -v
python run_both_browsers.py test_01_first_test.py --headed --slowmo 350 -v
python run_both_browsers.py --collect-only -q
python run_both_browsers.py --run-public -v
python run_both_browsers.py --html=reports/both-browsers.html --self-contained-html --junitxml=reports/both-browsers.xml --tracing retain-on-failure --screenshot only-on-failure -v
```

These run browser-dependent tests on Chromium and Firefox. The direct API test runs once. Expected default outcome after successful execution: 71 passed and 4 skipped. Public tests enabled: 75 passed if the external sites remain available and match the examples. The runner returns pytest's exit code, so failures are not hidden. It uses the currently active Python and locates the bundle even when called from another directory.

All commands below using only `python -m pytest` default to Chromium unless a browser is explicitly selected. To use both engines, add `--browser chromium --browser firefox` or replace `python -m pytest` with `python run_both_browsers.py`.

## Install and verify

```sh
python -m pip install -r requirements.txt
python -m playwright install chromium firefox
python --version
python -m pip show playwright pytest-playwright pytest
python -m pytest --collect-only -q
python -m pytest -v
```

The two public-site tests are skipped by default. Parameterized examples create multiple test cases per file; a file count is not the same as a test-case count.

## One test, one file, or a subset

```sh
python -m pytest test_02_id.py -v
python -m pytest test_16_dialogs.py::test_confirm_accept -v
python -m pytest test_21_parametrize.py -v
python -m pytest test_21_parametrize.py -k wrong-password -v
python -m pytest -m smoke -v
python -m pytest -k login -v
python -m pytest -x -v
python -m pytest --maxfail=2 -v
python -m pytest --lf -v
```

`-x` stops after the first failure; `--maxfail=2` stops after two. `--lf` reruns failures recorded in pytest's local cache; if there are no recorded failures it normally runs all tests. Use `--lf --lfnf=none` if you want no tests when the cache has no failures.

## Visible teaching run

```sh
python -m pytest test_11_login.py --headed --slowmo 500 -v
```

For quicker verification remove `--headed` and `--slowmo`. A test's page/context closes at teardown; this is expected.

## Inspector and debugging

macOS / Linux:

```sh
PWDEBUG=1 python -m pytest test_11_login.py -s
```

Windows Command Prompt (the second set command clears the setting afterward):

```bat
set PWDEBUG=1
python -m pytest test_11_login.py -s
set PWDEBUG=
```

Windows PowerShell:

```powershell
$env:PWDEBUG="1"
python -m pytest test_11_login.py -s
Remove-Item Env:PWDEBUG
```

Alternatively add `lab.pause()` temporarily inside a test, then run with `--headed -s`. Remove it after the demo. Use Inspector's step/resume controls. `-s` exposes printed output. Inspect a failing assertion before extending timeouts.

## Code generation and locator picking

Terminal 1:

```sh
python server.py --port 8000
```

Terminal 2, in the same bundle with the environment active:

```sh
python -m playwright codegen --target python-pytest http://127.0.0.1:8000
```

Record login, pick a locator, and compare generated code with test_11_login.py. Add meaningful assertions and adapt navigation to `lab_url`/`lab` before saving a generated test into this bundle. Generated code is a starting point and still needs review.

## Screenshots, video, traces, and reports

```sh
python -m pytest -v --screenshot only-on-failure --tracing retain-on-failure --video retain-on-failure --output test-results
python -m pytest test_11_login.py -v --tracing on --output test-results
python -m pytest -v --html=reports/report.html --self-contained-html --junitxml=reports/results.xml
```

Artifacts are below `test-results/`, grouped into per-test directories; pytest-playwright chooses their names. The trace from a specific test is a `trace.zip` within its test directory. Replace the sample path below with that actual path:

```sh
python -m playwright show-trace test-results/ACTUAL-TEST-DIRECTORY/trace.zip
```

`--tracing on` records passing tests too and is useful for an initial trace demo. `retain-on-failure` keeps only failures; a fully passing run will not leave retained traces/videos. Open `reports/report.html` in a browser. The HTML plugin generates result summaries; traces/videos stay separate and are not automatically embedded in that report. JUnit XML is suitable for CI ingestion.

The options apply to contexts/pages created by plugin fixtures. Example 24 uses the plugin new_context fixture for its restored context, preserving the selected browser and plugin artifact management. The manually created API context in example 28 is browser independent.

## Chromium and Firefox separately or together

```sh
python -m playwright install chromium firefox
python -m pytest --browser chromium -v
python -m pytest --browser firefox -v
python -m pytest --browser chromium --browser firefox -v
```

Install both engines before class. Reinstall browser binaries after upgrading Playwright. Public tests are skipped by default on both engines, not just one. No browser-dependent test has an engine-specific skip.

## Viewport sizes and parallel execution

```sh
python -m pytest test_29_viewport.py --browser chromium --browser firefox -v
python run_both_browsers.py -n 2 -v
```

Example 29 tests desktop and narrow viewports on both engines. A viewport size is not full mobile-device emulation. Avoid combining an iPhone/mobile profile with Firefox: Firefox does not support the is_mobile context option. Keep the shared classroom examples on desktop browser contexts and vary their viewport size.

Two parallel workers are enough for demonstrating xdist. Each worker gets its own local server on a free port, and tmp_path keeps file artifacts isolated. Avoid parallel headed demonstrations if multiple windows distract the audience.

## Optional public-site examples

```sh
python -m pytest test_31_public_example.py --run-public --headed -v
python -m pytest test_32_public_todomvc.py --run-public --headed --slowmo 350 -v
python run_both_browsers.py -m public --run-public -v
```

Internet is required. `--run-public` enables public tests; `-m public` selects only them. With `--run-public` alone the local tests are still included unless you select files or markers.

## Cleanup

Stop a manually started server with Ctrl+C. Deactivate the environment after class:

```sh
deactivate
```
