# Simple Playwright: public website examples

Ten small examples, each written twice: synchronous Python and asynchronous Python. Examples 01–08 use the public Playwright TodoMVC demo at https://demo.playwright.dev/todomvc/. Examples 09–10 use Selenium’s public practice form at https://www.selenium.dev/selenium/web/web-form.html. No local website server, pytest, conftest.py, account, or credentials are needed. Internet access is required.

## Setup

Use Python 3.10+ for a new installation. Open a terminal in this extracted bundle folder.

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Windows Command Prompt:

```bat
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m playwright install chromium
```

PowerShell activation: `.\.venv\Scripts\Activate.ps1`.
On Linux, missing browser libraries can require `python -m playwright install --with-deps chromium` with the appropriate system permissions.

## Start with these two commands

```bash
python sync/01_open_website.py
python async/01_open_website.py
```

Each command opens a browser window, performs its assertions, prints PASS, and closes the browser. The window closes quickly because the example is complete. No fixed sleep is needed. Visible actions use a small slow_mo delay for teaching.

## Examples

| Number | Filename in both folders | Learn |
|---|---|---|
| 01 | 01_open_website.py | Navigate, title, heading |
| 02 | 02_add_todo.py | Fill a textbox and press Enter |
| 03 | 03_complete_todo.py | Check a checkbox |
| 04 | 04_filter_todos.py | Click links and verify lists |
| 05 | 05_edit_todo.py | Double-click and edit |
| 06 | 06_delete_todo.py | Hover and click Delete |
| 07 | 07_clear_completed.py | Clear finished tasks |
| 08 | 08_reload_persistence.py | Reload and localStorage persistence |
| 09 | 09_dropdown.py | Dropdown selection and checkbox state |
| 10 | 10_submit_form.py | Fill and submit a practice form |

Example commands:

```bash
python sync/02_add_todo.py
python async/02_add_todo.py
python sync/04_filter_todos.py
python async/05_edit_todo.py
```

## Run the whole bundle

```bash
python run_all.py
python run_all.py --mode sync
python run_all.py --mode async
python run_all.py --headless
```

The default runs all ten sync examples followed by all ten async examples. Expected successful summary: **20 passed; 0 failed**. Failures print their traceback, the runner continues to show all results, and its final exit code is nonzero if any example fails.

Run one example without a window:

```bash
python async/02_add_todo.py --headless
```

## Chromium or installed Google Chrome

Default: Playwright's bundled Chromium, a separate browser built from the same open-source engine used by Chrome. Firefox is never selected.

For your installed Google Chrome, add `--chrome`:

```bash
python sync/02_add_todo.py --chrome
python async/02_add_todo.py --chrome
python run_all.py --chrome --headless
```

The --chrome option requires Google Chrome to be installed. It creates a fresh automation context rather than using your personal browser profile.

## Read the examples

Each script contains its complete imports, browser setup, actions, assertions, and cleanup. There are no hidden fixtures or shared helpers to understand first. The duplicate setup is intentional so you can copy and run one file independently.

Read EXPLAINED.md for a plain-language walkthrough and a sync-versus-async comparison. VALIDATION.md records actual execution results.

## Isolation and public-site behavior

Every script creates a new browser context with empty browser storage. The form submissions contain only demo text. Todo items stay in that isolated context's localStorage, and the context is closed at the end. No shared account or database is changed. Example 08 keeps its own context while reloading, so its item persists across the reload.

Public sites can become unavailable or change their HTML. The assertions expose those failures instead of hiding them. These examples do not disable HTTPS validation or silently skip failed assertions.

## Troubleshooting

| Symptom | Fix |
|---|---|
| No module named playwright | Activate the same environment and install requirements.txt |
| Browser executable missing | Run python -m playwright install chromium |
| Google Chrome channel missing | Install Chrome or omit --chrome to use bundled Chromium |
| Website navigation fails | Open the demo URL manually and check network/proxy access |
| Window closes | Normal: the script closes it after its checks; see terminal output |
| asyncio.run cannot run inside an event loop | Run the file from a terminal; notebook use requires adapting the entry point |

## Official references

- Public testing demo: https://demo.playwright.dev/todomvc/
- Python sync and async usage: https://playwright.dev/python/docs/library
- Locators: https://playwright.dev/python/docs/locators
- Assertions: https://playwright.dev/python/docs/test-assertions
