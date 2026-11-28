# Trainer delivery notes

## Opening 10 minutes

Ask what a manual login check needs: open the site, find username and password, fill, submit, verify the outcome. Map those steps onto example 11, then start teaching from example 01.

Explain the object hierarchy: Playwright controls a browser engine; a browser owns contexts; each context is an isolated cookie/storage session; each page is a tab; a locator identifies elements inside a page. pytest discovers test functions and injects requested fixtures. conftest.py provides the local-site fixtures. Use the synchronous API consistently: do not mix async/await into these tests.

Open the local site using `python server.py --port 8000`, then inspect Username using the browser's Inspect command. Show id, name, classes, placeholder, label, and data-testid. Have learners identify which attribute each locator uses. Automated test windows use their own server and isolated context; typing into the manually opened site does not seed a test.

## What to say for every example

1. State the observable outcome in its “Achieve” line.
2. Inspect only the relevant HTML or browser behavior.
3. Point to the locator, action, and assertion in the test.
4. Ask learners to predict the result.
5. Run the file with its documented command.
6. Try the exercise or explain the expected change.

Read EXAMPLE_GUIDE.md alongside the source files. Keep the source visible while teaching; the comments/docstrings explain why the code works, not just what to type.

## Final 20 minutes

**Inspector — 5 minutes:** Run example 11 with PWDEBUG=1 using the platform-specific command from COMMANDS.md. Step through fill and click, pick a locator, and explain why inspection is useful before changing a selector. Resume to finish; remove any temporary pause.

**Failure evidence and report — 5 minutes:** Temporarily change the expected welcome text in example 11 to `Welcome, wrong-user!`, then run:

```sh
python -m pytest test_11_login.py -v --screenshot only-on-failure --tracing retain-on-failure --video retain-on-failure --html=reports/failure-demo.html --self-contained-html --output test-results
```

Show the assertion's expected and received values, find the per-test trace.zip, and open it using the command in COMMANDS.md. Show the HTML summary and explain that the trace and video are separate files. Restore `Welcome, tester!`, rerun, and confirm it passes. Never leave the deliberate failing version in the supplied bundle.

**Learner recap — 10 minutes:** Give a mini-task: change the journey to choose Mouse and United Kingdom, add an unknown-user login parameter, and run only smoke tests. Ask learners to explain why selecting all Add to cart buttons is ambiguous, why a plain Python assert differs from a retrying Playwright expect, and why each test gets fresh storage.

## Troubleshooting

| Symptom | What to check |
|---|---|
| `No module named pytest` or playwright | Activate the intended environment; install requirements with that environment's Python. |
| Fixture `page` not found or unrecognized Playwright flags | pytest-playwright must be installed in the same environment used by `python -m pytest`. |
| Browser executable missing | Run `python -m playwright install chromium firefox` in the active environment. Repeat browser installation after upgrading Playwright. |
| Missing Linux shared libraries | Use the system-dependency installation command in README.md. |
| Browser opens and immediately closes | The test finished and fixture teardown closed it; use Inspector to step through. |
| Strict mode violation | The locator matches multiple elements. Scope to the intended region or item. |
| Locator timeout | Verify page, frame, label/name, visibility, and intended UI condition. Use the trace before increasing timeouts. |
| Public-site failure | Check connectivity and current external DOM; switch to the local equivalent for class. |
| No screenshots/videos/traces after passing run | Failure-only retention intentionally discards them. Use `--tracing on` for a passing trace demo. |
| Manual site refuses connection | Start server.py and confirm the port. Automated tests start their own server. |
| Address already in use for manual site | Start with `--port 8001`, then change the manual/codegen URL. |
| `python test_*.py` produces no output | Use `python -m pytest FILE.py -v` to collect and execute test functions. |
| Firefox rejects a mobile option | Do not pass an iPhone/mobile device profile to the shared suite. Example 29 varies viewport size and supports both engines. |

## Scope and next steps

This session covers browser-testing foundations and selected advanced demonstrations. Further workshops can add real authentication, accessibility checks, visual regression baselines, richer custom dropdowns, drag/drop behavior, CI workflows, and backend test-data management. The practice site is intentionally a small local teaching application.

## Cross-browser classroom check

Before class, run `python run_both_browsers.py -v`. In verbose output, show the `[chromium]` and `[firefox]` cases for the same function. Demonstrate the first example with `python run_both_browsers.py test_01_first_test.py --headed --slowmo 350 -v`. For teaching one engine at a time, use the explicit `--browser chromium` or `--browser firefox` pytest command in COMMANDS.md.

Default expected collection: 75 cases, comprising 71 local executions and 4 optional public cases skipped. The direct API test runs once and does not open either browser. Browser-dependent tests and their assertions are shared across the engines; no engine-specific skip masks an unsupported example.
