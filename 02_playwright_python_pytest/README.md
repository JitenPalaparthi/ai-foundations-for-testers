# 2. Playwright with Python + pytest — 4-hour demonstration bundle

This module follows Python Foundations for Testers. The requested delivery duration is **4 hours (240 minutes)**, even though the module label included “3”. Use the synchronous Playwright API throughout to keep beginner examples consistent.

## What learners will achieve

By the end, learners can create and run a browser test, choose a suitable locator, interact with forms, verify browser outcomes, handle delayed UI and browser events, parameterize tests, reuse fixtures and page objects, inspect/mock an API response, and capture a report and failure evidence.

The bundle includes **30 core example files** plus **2 optional public-site examples**. Every test file has its objective, run command, explanation, expected result, and an exercise at the top. The local practice site covers all core examples and starts automatically for tests. It needs no internet after dependency and browser installation.

## Setup — before class

Use Python 3.10+ for a fresh installation. Open a terminal in this directory. Setup and browser downloads should be completed before the four-hour session.

macOS / Linux:

```sh
cd "/Users/jiten/Documents/ChatGPT/AI-For-Testers/02_playwright_python_pytest"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium firefox
python run_both_browsers.py -v
```

Windows Command Prompt (replace the example path with your extracted bundle location):

```bat
cd C:\training\02_playwright_python_pytest
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m playwright install chromium firefox
python run_both_browsers.py -v
```

For Windows PowerShell, activate with `.\.venv\Scripts\Activate.ps1`. If local policy prevents activation, invoke `.\.venv\Scripts\python.exe` directly for each command. On Linux, if browser system libraries are missing, use `python -m playwright install --with-deps chromium firefox` with the system permissions your machine requires.

## Four-hour delivery schedule

| Time | Topic | Demonstration |
|---|---|---|
| 00:00–00:10 | Introduction | Browser → context → page → locator; read first test and fixture |
| 00:10–01:10 | Locators | Examples 01–10; 6 minutes each |
| 01:10–02:10 | Browser interactions | Examples 11–20; 6 minutes each |
| 02:10–02:20 | Break | 10 minutes |
| 02:20–03:00 | pytest structure | Examples 21–25; 8 minutes each |
| 03:00–03:40 | API and integrated flows | Examples 26–30; 8 minutes each |
| 03:40–04:00 | Debugging, reporting, practice | Inspector 5 minutes; failure trace/report 5; learner recap 10 |

Total: 10 + 60 + 60 + 10 + 40 + 40 + 20 = **240 minutes**. Public examples 31–32 are optional extensions or substitutes, not extra required material inside this schedule.

For each 6-minute demo: state the goal (30 seconds), inspect the relevant HTML (1 minute), explain the test (90 seconds), run it and inspect the outcome (1 minute), and try or discuss the exercise (2 minutes). For each 8-minute demo add 2 minutes of learner practice. This is a broad demonstration workshop; use the exercises as follow-up when a group needs more practice time.

## Run on Chromium and Firefox

```sh
python -m playwright install chromium firefox
python run_both_browsers.py -v
python run_both_browsers.py test_01_first_test.py -v --headed --slowmo 350
python run_both_browsers.py --run-public -v
```

The runner is equivalent to `python -m pytest --browser chromium --browser firefox` followed by your options. Browser-dependent cases run on each engine. The direct API example has no browser dependency and runs once. Without `--run-public`, collection contains 75 cases: 71 local executions and 4 skipped public executions. With public tests enabled, all 75 are selected for execution. These are expected counts, not a claim that this machine completed the browser runs.

For a single browser, use `python -m pytest --browser chromium -v` or `python -m pytest --browser firefox -v`. Keep `pytest.ini` free of fixed browser options so these explicit choices remain easy to use.

Both engines must be installed through Playwright; a regular Firefox installation is not a substitute for Playwright's patched Firefox. Example 29 uses viewport sizes and does not require mobile emulation, which Firefox does not support. Browser-specific screenshots and pixel differences are not compared to a shared baseline.

## Start demonstrating

```sh
python -m pytest test_01_first_test.py --browser chromium --browser firefox -v --headed --slowmo 350
python -m pytest test_02_id.py --browser chromium --browser firefox -v --headed --slowmo 350
python -m pytest test_11_login.py --browser chromium --browser firefox -v --headed --slowmo 350
python -m pytest test_21_parametrize.py --browser chromium --browser firefox -v --headed --slowmo 350
```

`--headed` shows the browser. `--slowmo 350` slows Playwright operations for teaching; it is not a synchronization technique. Tests otherwise run headless. Run the files with pytest, not `python test_01_first_test.py`; executing a test file directly only defines its functions.

To inspect the site manually or use codegen, start it in a separate terminal:

```sh
python server.py --port 8000
```

Open **http://127.0.0.1:8000**. Stop the server with Ctrl+C. Keep this terminal open while using codegen. Automated tests start their own server on a free port, so they do not require this command and do not use your manually opened tab. If 8000 is occupied, choose `--port 8001` and update your manual URL/codegen command.

## Where to look

- `EXAMPLE_GUIDE.md`: objectives, commands, walkthroughs, and expected results for every example.
- `COMMANDS.md`: setup, single-test runs, debugging, codegen, reports, traces, browsers, devices, and parallel execution.
- `LOCATOR_CHEATSHEET.md`: ID, class, name, CSS, XPath, and user-facing locator syntax with pitfalls.
- `TRAINER_NOTES.md`: opening explanation, HTML inspection, deliberate-failure exercise, recap, and troubleshooting.
- `EXERCISE_SOLUTIONS.md`: suggested practice answers.
- `run_both_browsers.py`: runs the chosen tests on both requested browser engines.
- `conftest.py`: local server lifecycle, navigation/login fixtures, and public-test opt-in.
- `pages.py`: the shared login Page Object.
- `practice_site/`: the local sample app and downloadable CSV.
- `VALIDATION.md`: actual executed checks and installed versions.

This practice application simulates login with a local-storage flag, displays the chosen upload filename, and exposes one read-only JSON endpoint. These are teaching behaviors, not production authentication, file storage, or a real shopping checkout.

## Validation status

The API example and static checks pass. Browser execution status and the exact two-browser collection counts are recorded in VALIDATION.md. The examples use the selected browser fixture and portable locator/action APIs; no browser-dependent example is intentionally skipped on Chromium or Firefox. Public tests remain optional because they require external sites.

## Example index

| Example | Achieve | Minutes |
|---|---|---:|
| [test_01_first_test.py](test_01_first_test.py) | Navigate to a page and verify its title and heading. | 6 |
| [test_02_id.py](test_02_id.py) | Fill a uniquely identified field. | 6 |
| [test_03_class.py](test_03_class.py) | Use one or multiple CSS classes. | 6 |
| [test_04_attributes_css.py](test_04_attributes_css.py) | Find elements by HTML attributes and CSS relationships. | 6 |
| [test_05_role.py](test_05_role.py) | Locate controls as an assistive technology user would. | 6 |
| [test_06_label_placeholder.py](test_06_label_placeholder.py) | Locate form fields using their visible meaning. | 6 |
| [test_07_text_alt_title.py](test_07_text_alt_title.py) | Find messages, images, and tooltip metadata. | 6 |
| [test_08_testid_xpath.py](test_08_testid_xpath.py) | Compare explicit test contracts with structural selectors. | 6 |
| [test_09_filter_scope.py](test_09_filter_scope.py) | Click the correct button when several share a name. | 6 |
| [test_10_lists_tables.py](test_10_lists_tables.py) | Assert repeated items and inspect a table row. | 6 |
| [test_11_login.py](test_11_login.py) | Automate a complete login outcome. | 6 |
| [test_12_checkbox_radio.py](test_12_checkbox_radio.py) | Set and verify state deterministically. | 6 |
| [test_13_dropdown.py](test_13_dropdown.py) | Select by value, label, and index. | 6 |
| [test_14_keyboard_mouse.py](test_14_keyboard_mouse.py) | Exercise event-driven interactions. | 6 |
| [test_15_auto_wait.py](test_15_auto_wait.py) | Wait for behavior instead of sleeping. | 6 |
| [test_16_dialogs.py](test_16_dialogs.py) | Register a handler before the dialog opens. | 6 |
| [test_17_iframe.py](test_17_iframe.py) | Locate a control in a separate document. | 6 |
| [test_18_popup.py](test_18_popup.py) | Capture the new page event before clicking. | 6 |
| [test_19_upload_download.py](test_19_upload_download.py) | Provide a local file and verify downloaded content. | 6 |
| [test_20_assertions_screenshots.py](test_20_assertions_screenshots.py) | Verify text, values, state, attributes, URL, and evidence. | 6 |
| [test_21_parametrize.py](test_21_parametrize.py) | Run valid, invalid, and empty login inputs. | 8 |
| [test_22_fixtures_isolation.py](test_22_fixtures_isolation.py) | Reuse setup and prove storage starts clean. | 8 |
| [test_23_page_objects.py](test_23_page_objects.py) | Move repeated selectors and actions into a reusable object. | 8 |
| [test_24_storage_state.py](test_24_storage_state.py) | Save and load browser storage into an isolated context. | 8 |
| [test_25_markers.py](test_25_markers.py) | Run a smoke subset or a named test. | 8 |
| [test_26_network_response.py](test_26_network_response.py) | Wait for a specific request and verify UI plus payload. | 8 |
| [test_27_mock_api.py](test_27_mock_api.py) | Make the browser render controlled test data. | 8 |
| [test_28_api_request.py](test_28_api_request.py) | Check an API without a page interaction. | 8 |
| [test_29_viewport.py](test_29_viewport.py) | Exercise desktop and narrow layouts. | 8 |
| [test_30_capstone.py](test_30_capstone.py) | Combine login, preferences, product choice, and API output. | 8 |
| [test_31_public_example.py](test_31_public_example.py) | Apply locators to an external page. | Optional |
| [test_32_public_todomvc.py](test_32_public_todomvc.py) | Create, complete, and remove a todo item. | Optional |

## Official references

The bundle uses the official pytest plugin and locator APIs. See [installation](https://playwright.dev/python/docs/intro), [locators](https://playwright.dev/python/docs/locators), [pytest plugin and CLI options](https://playwright.dev/python/docs/test-runners), and [network testing](https://playwright.dev/python/docs/network). Optional external examples use [Example Domain](https://example.com) and [Playwright TodoMVC](https://demo.playwright.dev/todomvc/). External pages need internet and may change; verify them before class.
