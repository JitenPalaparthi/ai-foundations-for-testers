# Live execution results

Validated on 20 November 2026 on macOS arm64.

- Python: 3.9.6 in an isolated validation environment; Python 3.10+ recommended for new installations.
- Playwright: 1.60.0 (pinned in requirements.txt).
- Chromium: 148.0.7778.96, Playwright build 1223.
- Full command: `python run_all.py --headless`.
- Actual result: **20 passed; 0 failed**, runner exit code 0.
- Both public websites were reached over HTTPS by real Chromium browser instances.
- All 10 sync and 10 async scripts executed their actual browser interactions and assertions.
- No browser mocking, local substitute website, disabled HTTPS validation, or test skipping was used.
- Extra visible-window checks: sync/02_add_todo.py and async/02_add_todo.py both passed with default headed settings.
- All 21 Python source files parsed successfully.

## Coverage

| Example | Sync | Async |
|---|---|---|
| Open website and title/heading assertions | PASS | PASS |
| Add todo | PASS | PASS |
| Complete todo | PASS | PASS |
| Active/Completed/All filters | PASS | PASS |
| Edit todo | PASS | PASS |
| Delete todo | PASS | PASS |
| Clear completed | PASS | PASS |
| Reload persistence | PASS | PASS |
| Dropdown and checkbox | PASS | PASS |
| Submit public practice form | PASS | PASS |

## Evidence and limits

`validation-all.log` contains the successful complete run. `validation-headed.log` contains the two extra visible-window checks.

Installed Google Chrome (--chrome) was not validated because it is not installed on this machine. The default bundled Chromium path was validated. Firefox is not used.

Public websites can change or become unavailable after this run. The bundled assertions and runner will report those failures rather than claim success.
