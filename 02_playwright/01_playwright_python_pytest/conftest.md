# Understanding conftest.py and automatic pytest fixtures

This guide explains the project's actual `conftest.py`: where its code executes, how pytest discovers it, when each function runs, how fixtures depend on one another, and how the local practice website works.

## 1. What is conftest.py?

`conftest.py` is a special Python filename recognized by pytest. It holds shared fixtures and hooks for tests in its directory and descendant directories.

You run tests, not conftest.py:

```bash
cd /Users/jiten/Documents/ChatGPT/AI-For-Testers/02_playwright_python_pytest
python -m pytest test_01_first_test.py --browser chromium --headed -v
```

The project's convenience runner also starts pytest:

```bash
python run_chrome.py test_01_first_test.py --headed -v
```

You do not need `import conftest` in your tests. Do not run `python conftest.py` to start the website: importing or executing this file defines its functions but does not ask pytest to execute its fixtures.

## 2. The complete file

```python
"""Shared pytest fixtures. No separate server command is needed for tests."""
from threading import Thread
import pytest
from server import make_server


def pytest_addoption(parser):
    parser.addoption("--run-public", action="store_true", default=False,
                     help="Include optional internet-dependent public-site tests")


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-public"):
        skip = pytest.mark.skip(reason="Use --run-public to enable internet examples")
        for item in items:
            if "public" in item.keywords:
                item.add_marker(skip)


@pytest.fixture(scope="session")
def lab_url():
    server = make_server()
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}"
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)


@pytest.fixture
def lab(page, lab_url):
    page.goto(lab_url)
    return page


@pytest.fixture
def logged_in_page(lab):
    lab.get_by_label("Username", exact=True).fill("tester")
    lab.get_by_label("Password", exact=True).fill("secret123")
    lab.get_by_role("button", name="Sign in", exact=True).click()
    return lab
```

## 3. Where does everything run?

| Component | Execution location | Responsibility |
|---|---|---|
| pytest | Python process on your computer | Discover tests, resolve fixtures, execute tests, report results |
| conftest.py hooks and fixtures | Same pytest Python process | Configure selection, prepare resources, clean up |
| Local HTTP server | Background thread inside that process | Listen for browser requests |
| HTTP request handling | Worker threads created by ThreadingHTTPServer | Serve files and the API |
| Browser | Separate browser process controlled through Playwright | Render the website and execute JavaScript |
| index.html JavaScript | Inside the browser page | Handle login, buttons, dialogs, localStorage, API fetches |

A background thread is not a separate Python process. It lets the server wait for requests while pytest continues running tests.

## 4. How pytest discovers and uses this file automatically

1. You invoke pytest from the command line, directly or through `run_chrome.py`.
2. Pytest loads applicable plugins and discovers applicable `conftest.py` files. A conftest in a test directory applies to tests below that directory; unrelated sibling directories do not inherit its fixtures.
3. Python imports this file. Imports and function definitions execute, and `@pytest.fixture` marks the decorated functions for pytest fixture registration. The fixture bodies do not run yet.
4. The early `pytest_addoption` hook registers the project's command-line option.
5. Pytest collects test functions from files such as `test_01_first_test.py`.
6. `pytest_collection_modifyitems` adjusts the collected items, marking optional public tests to skip when needed.
7. Before each test, pytest resolves the fixtures requested by its parameter names, including dependencies requested by other fixtures.
8. Pytest executes fixture setup and passes the produced values into the test.
9. Pytest executes the test body, then performs the applicable fixture teardown. Session resources remain until session teardown.

Pytest's plugin system recognizes the hook names. Fixture lookup recognizes registered fixture names. These are two different mechanisms.

### Hooks versus fixtures

| Function | Kind | Trigger |
|---|---|---|
| pytest_addoption | Hook | Command-line configuration |
| pytest_collection_modifyitems | Hook | After test collection |
| lab_url | Session fixture | First test or fixture requesting it |
| lab | Function fixture | Each test requesting it directly or indirectly |
| logged_in_page | Function fixture | Each test requesting it directly or indirectly |

None of these three fixtures uses `autouse=True`. They run only when requested, directly or through another fixture. A browser-independent test can request `lab_url` without requesting a browser.

## 5. Imports and module docstring

```python
"""Shared pytest fixtures. No separate server command is needed for tests."""
```

This is the module's documentation string. It describes the purpose of the file; it does not start a server.

```python
from threading import Thread
```

Imports Python's thread class to run the server in the background.

```python
import pytest
```

Provides fixture decorators, markers, and pytest APIs.

```python
from server import make_server
```

Imports the `make_server` function from the project's `server.py`. Importing that module does not execute its `if __name__ == "__main__"` block, so importing it does not start the manual server on port 8000.

## 6. pytest_addoption: registering --run-public

```python
def pytest_addoption(parser):
    parser.addoption("--run-public", action="store_true", default=False,
                     help="Include optional internet-dependent public-site tests")
```

`parser` is provided by pytest's hook system. This function adds a custom CLI switch.

| Argument | Meaning |
|---|---|
| --run-public | Name typed on the command line |
| action="store_true" | Presence of the switch sets the value to True |
| default=False | Without the switch, the value is False |
| help=... | Description shown in pytest help |

```bash
# Public examples will be skipped.
python -m pytest -v

# Public examples are allowed to run alongside local tests.
python -m pytest --run-public -v

# Select only public examples and allow them to run.
python -m pytest -m public --run-public -v
```

`--run-public` does not itself select only public tests. Selection and permission to run these optional examples are separate settings.

## 7. pytest_collection_modifyitems: skipping optional public tests

```python
def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-public"):
        skip = pytest.mark.skip(reason="Use --run-public to enable internet examples")
        for item in items:
            if "public" in item.keywords:
                item.add_marker(skip)
```

Pytest supplies both arguments:

- `config`: pytest configuration, including parsed command-line values.
- `items`: collected test items. Parameterized cases appear as separate items.

When `--run-public` is absent, the code creates a skip marker, visits collected items, and adds that marker to items carrying the `public` keyword. In this project, public tests are identified with `@pytest.mark.public`.

```python
@pytest.mark.public
def test_external_site(page):
    page.goto("https://example.com")
```

The test is still collected and appears as skipped. It is not removed from collection. Under normal pytest execution, a skipped test does not proceed to its fixture setup or test body.

## 8. lab_url: starting the local server

```python
@pytest.fixture(scope="session")
def lab_url():
```

The decorator registers a fixture named `lab_url`. Session scope means pytest sets it up once when first requested and reuses its yielded URL during that pytest session. It is not automatically started merely because pytest has begun.

```python
server = make_server()
```

The relevant function in `server.py` is:

```python
def make_server(port=0):
    return ThreadingHTTPServer(
        ("127.0.0.1", port),
        partial(Handler, directory=str(SITE)),
    )
```

`127.0.0.1` is the loopback address of your own computer. Port `0` asks the operating system to allocate an available port. The actual assigned port is available through `server.server_port`.

For example, the resulting URL might be `http://127.0.0.1:54321`. A later run may get a different port. The server is bound to loopback, so it is intended for local access.

```python
thread = Thread(target=server.serve_forever, daemon=True)
```

Creates a background thread whose work is `server.serve_forever`.

Notice that `target=server.serve_forever` passes a callable. Writing `target=server.serve_forever()` would call the server loop immediately in the current thread, preventing normal setup from continuing.

`daemon=True` means this thread alone will not keep the Python process alive after its non-daemon threads exit. Explicit cleanup is still performed below.

```python
thread.start()
```

Starts that thread. The HTTP server can now accept and handle requests while pytest continues.

```python
yield f"http://127.0.0.1:{server.server_port}"
```

Supplies the URL to requesting tests or fixtures. `yield` pauses this fixture at that point. The server continues running in its background thread.

```python
server.shutdown()
server.server_close()
thread.join(timeout=5)
```

These lines execute during session teardown, after tests using the session finish:

1. `shutdown()` asks the server's `serve_forever()` loop to stop.
2. `server_close()` closes server resources, including its listening socket.
3. `join(timeout=5)` waits up to five seconds for the serving thread to exit.

The five seconds is a maximum wait, not an unconditional five-second sleep. Also, it bounds only `join`, not the entire teardown sequence.

### Why yield instead of return?

A yield fixture supports setup before `yield` and cleanup after `yield`.

```python
@pytest.fixture
def resource():
    value = prepare_resource()
    yield value
    clean_up_resource(value)
```

A normal `return` ends a function immediately. Cleanup written after `return` would be unreachable.

After a fixture has successfully reached `yield`, pytest normally runs its teardown even if a test assertion fails. Abrupt process termination cannot guarantee cleanup. If setup fails before reaching `yield`, this fixture's post-yield cleanup is not registered as completed setup.

## 9. lab: opening the website for each test

```python
@pytest.fixture
def lab(page, lab_url):
    page.goto(lab_url)
    return page
```

Without an explicit scope, `@pytest.fixture` defaults to `scope="function"`: one fixture instance per requesting test invocation.

The parameter names declare dependencies:

| Dependency | Defined by | Value supplied |
|---|---|---|
| page | pytest-playwright plugin | A Playwright Page in an isolated browser context |
| lab_url | This conftest.py | URL of the running local server |

Pytest resolves both before executing the `lab` body. `page.goto(lab_url)` navigates the browser tab to the site. `return page` supplies that same Page object to the test.

```python
from playwright.sync_api import expect


def test_login_heading(lab):
    expect(lab.get_by_role("heading", name="Login", exact=True)).to_be_visible()
```

The returned object is a Page, not a fixture function. Therefore, `lab.get_by_role(...)` is correct inside the test; `lab()` is not required.

The plugin owns browser context/page cleanup. This fixture does not need to close the page itself.

## 10. logged_in_page: reusing login preparation

```python
@pytest.fixture
def logged_in_page(lab):
    lab.get_by_label("Username", exact=True).fill("tester")
    lab.get_by_label("Password", exact=True).fill("secret123")
    lab.get_by_role("button", name="Sign in", exact=True).click()
    return lab
```

This fixture first requests `lab`, which already requests `page` and `lab_url`.

1. Find the input associated with the exact label `Username` and fill it.
2. Find the input associated with the exact label `Password` and fill it.
3. Find the button whose accessible name is exactly `Sign in` and click it.
4. Return the same browser Page to the test.

`exact=True` requires an exact accessible label/name match instead of a partial text match. Playwright locators and actions provide their own waiting behavior; this code does not use fixed sleeps.

```python
from playwright.sync_api import expect


def test_welcome(logged_in_page):
    expect(logged_in_page.get_by_role("status")).to_have_text(
        "Welcome, tester!"
    )
```

The fixture performs the login action. The test's assertion verifies the resulting state and retries until it matches or times out.

## 11. How fixture dependency injection works

Consider:

```python
def test_welcome(logged_in_page):
    ...
```

Pytest does not expect you to pass a normal function argument manually. It inspects the test's parameter names and looks them up in its fixture registry.

To provide `logged_in_page`, it needs `lab`. To provide `lab`, it needs both `page` and `lab_url`. Those dependencies must be ready before their dependents run.

| Resource | Must be ready before |
|---|---|
| Browser page (`page`) | lab |
| Running server URL (`lab_url`) | lab |
| Navigated page (`lab`) | logged_in_page |
| Page after login (`logged_in_page`) | Test body |

There is no necessary dependency ordering between `page` and `lab_url` themselves. Do not assume their relative setup order from the order in the parameter list. Both must be ready before `lab` runs.

Fixture order is based on scopes, dependencies, and autouse behavior—not simply on the order definitions appear in the file.

A misspelled parameter produces a fixture lookup error:

```python
def test_example(logged_in_pages):  # No fixture with this name.
    pass
```

Typical error: `fixture 'logged_in_pages' not found`.

## 12. What happens across two tests?

```python
def test_one(lab):
    ...


def test_two(logged_in_page):
    ...
```

| Resource | First test | Second test |
|---|---|---|
| lab_url server | Created if first requested here | Same server and URL reused |
| Browser process | Normally reused by the plugin for the selected engine | Normally reused |
| Browser context and page | Fresh isolated context/page | Another fresh isolated context/page |
| lab navigation | Opens local website | Opens local website again |
| Login action | Not requested | Performed by logged_in_page |

Browser isolation means the second test does not inherit the first test's cookies and localStorage by default. The server itself is shared, so mutable server-side state would require separate isolation if added later. The current users API returns fixed data.

Fixtures are cached within their scope. If one test requests both `lab` and `logged_in_page`, the `lab` dependency is resolved once for that test. Both names refer to the same page, and that page has undergone login before the test body begins.

With `pytest -n 2`, xdist creates separate worker processes. Each worker has its own session-scoped `lab_url` instance when needed, so there can be multiple local servers on separate available ports.

## 13. The first test uses fixtures directly

The project's first test has this shape:

```python
from playwright.sync_api import expect


def test_homepage(page, lab_url):
    page.goto(lab_url)
    expect(page).to_have_title("Tester Practice Lab")
    expect(
        page.get_by_role("heading", name="Tester Practice Lab", exact=True)
    ).to_be_visible()
```

This requests `page` and `lab_url` directly. It does not request `lab`, so the `lab` fixture body does not run. Navigation is done in the test instead.

Fixtures do not all execute for every test. Only the required dependency set is prepared, plus applicable autouse fixtures supplied by pytest/plugins or elsewhere.

## 14. Website structure and behavior

The website is a local training application named **Tester Practice Lab**.

| File or route | Purpose |
|---|---|
| server.py | Python HTTP server and users API handler |
| practice_site/index.html | Main page with inline CSS and JavaScript |
| practice_site/frame.html | Page embedded in the support iframe |
| practice_site/help.html | Help page opened in another tab |
| practice_site/report.csv | Sample download |
| GET /api/users | Fixed JSON response containing user Asha |

`SITE = Path(__file__).with_name("practice_site")` resolves the website directory relative to `server.py`, so serving files does not depend on the terminal's current working directory.

The API handler intercepts `/api/users` and returns JSON. Other GET requests are handled by `SimpleHTTPRequestHandler` using the practice_site directory.

```json
{"users": [{"id": 1, "name": "Asha"}]}
```

| Feature | What it does |
|---|---|
| Login | Checks tester / secret123 in browser JavaScript; displays a message |
| Saved session | Stores demo_user in localStorage after successful login |
| Restore session | Reads that localStorage flag and displays a message |
| Preferences | Country selection, terms checkbox, plan radio buttons, notes, Save |
| Search | Displays entered text after Enter is pressed |
| Products | Keyboard and Mouse cards with Add to cart buttons |
| Results table | Static TC01/PASS and TC02/FAIL rows |
| Delayed result | Shows Report ready after 350 milliseconds |
| Dialogs | Confirmation dialog and display-name prompt |
| Upload | Displays the chosen filename in the page |
| Download | Downloads report.csv |
| Hover and double click | Shows help text or updates an event message |
| Iframe | Embeds the support page |
| Load users | Fetches /api/users and renders the returned names |

There is no database or production authentication service. The login is a client-side exercise; the file input does not upload its contents to this server. Chromium renders the interface, while Python serves the files and API response.

## 15. Manual server versus automatic fixture server

| Mode | Command | Address | Lifecycle |
|---|---|---|---|
| Manual exploration | python server.py --port 8000 | http://127.0.0.1:8000 | Runs until Ctrl+C |
| Automated local tests | python run_chrome.py -v | http://127.0.0.1:<available-port> | Fixture starts and stops it |

When running the manual server, `server.py` executes its main block. Pytest is not involved, so the conftest fixtures do not run.

When running automated tests, pytest imports `make_server` and the fixture starts its own server. Tests do not attach to your manually opened Chrome tab or reuse your manual server on port 8000.

## 16. See fixture activity yourself

Run these commands from the project module directory with dependencies installed:

```bash
# List available fixtures, including plugin fixtures.
python -m pytest --fixtures -q

# Show the fixture setup plan without executing the tests.
python -m pytest test_01_first_test.py --setup-plan

# Show fixture setup/teardown while executing the test.
python -m pytest test_01_first_test.py --setup-show --headed -v

# Show fixtures required by each selected test.
python -m pytest test_01_first_test.py --fixtures-per-test

# Collect tests without normal test execution or fixture setup.
python -m pytest --collect-only -q

# Show custom command-line help, including --run-public.
python -m pytest --help
```

In `--setup-show` output, pytest uses scope abbreviations such as `S` for session and `F` for function. You will also see plugin fixtures beyond the three defined here.

For a temporary teaching demonstration, add print statements before and after `yield`, then run with `-s` to display them:

```python
@pytest.fixture(scope="session")
def lab_url():
    print("SETUP: starting local website server")
    server = make_server()
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = f"http://127.0.0.1:{server.server_port}"
    print("SERVER URL:", url)
    yield url
    print("TEARDOWN: stopping local website server")
    server.shutdown()
    server.server_close()
    thread.join(timeout=5)
```

```bash
python -m pytest test_01_first_test.py --headed --setup-show -s -v
```

This print-based snippet is an optional explanation aid; it does not modify the actual conftest.py supplied with this guide.

## 17. Common questions

**Why don't tests import lab_url?** Pytest discovers the fixture registration and injects its value by parameter name.

**Is page defined in this conftest.py?** No. pytest-playwright provides it. Install project dependencies with `python -m pip install -r requirements.txt` in the active environment.

**Does session scope mean the server is already running before collection?** No. This fixture starts when first requested during test setup.

**Does return page close the tab?** No. It gives the object to the requester. Plugin fixture teardown handles browser context/page cleanup.

**Does lab_url open a browser?** No. It only starts the server and yields its address. A browser is needed only if page or another browser fixture is requested.

**Does calling a fixture mean writing lab_url()?** Normally no. Declare `lab_url` as a parameter and let pytest manage its lifecycle.

**Can these fixtures be placed in a test file?** Yes, but they are then available to that module rather than automatically shared through the conftest directory hierarchy.

**Will collecting tests open the website?** `--collect-only` does not execute normal fixture setup or tests. Imports and collection hooks still run.

**Why is the server still available after lab returns?** Its separate session fixture is paused at yield and its background thread keeps serving until session teardown.

**Why doesn't pytest run every function in conftest.py?** Ordinary helper functions run only when called. Hooks run at their defined pytest lifecycle events; fixtures run when requested.
