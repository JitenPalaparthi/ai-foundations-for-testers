# Understanding these examples

## Sync first

```python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    try:
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.playwright.dev/todomvc/")
        entry = page.get_by_placeholder("What needs to be done?")
        entry.fill("Learn Playwright")
        entry.press("Enter")
        expect(page.get_by_test_id("todo-title")).to_have_text("Learn Playwright")
    finally:
        browser.close()
```

- `sync_playwright()` starts the Playwright driver and supplies its API.
- `p.chromium.launch()` launches a browser process.
- `new_context()` creates an isolated browser session with its own storage.
- `new_page()` opens a tab in that session.
- `goto()` navigates to the public website.
- `get_by_placeholder()` creates a locator for the textbox.
- `fill()` replaces the textbox text.
- `press("Enter")` sends the key that adds a todo.
- `get_by_test_id()` finds elements marked by the demo's data-testid attributes.
- `expect(...).to_have_text()` retries its assertion until the text matches or the timeout expires.
- `finally` closes the browser on success or failure.

In the sync API, Python waits for each Playwright call before continuing.

## Async equivalent

```python
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        try:
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto("https://demo.playwright.dev/todomvc/")
            entry = page.get_by_placeholder("What needs to be done?")
            await entry.fill("Learn Playwright")
            await entry.press("Enter")
            await expect(page.get_by_test_id("todo-title")).to_have_text("Learn Playwright")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
```

`async def` defines a coroutine function. `asyncio.run(main())` creates an event loop, runs this coroutine, and closes the loop. `await` lets the event loop run other ready asynchronous tasks while the current operation waits. The next dependent line continues after that operation completes.

An async script is not automatically concurrent. These examples deliberately run their dependent browser actions in order; they are not inherently faster than the sync versions.

## Which calls need await?

| Operation | Sync | Async |
|---|---|---|
| Launch | browser = p.chromium.launch() | browser = await p.chromium.launch() |
| Context | context = browser.new_context() | context = await browser.new_context() |
| Page | page = context.new_page() | page = await context.new_page() |
| Navigate | page.goto(url) | await page.goto(url) |
| Construct locator | entry = page.get_by_placeholder(text) | entry = page.get_by_placeholder(text) |
| Fill | entry.fill(text) | await entry.fill(text) |
| Click | locator.click() | await locator.click() |
| Title | page.title() | await page.title() |
| Assertion | expect(locator).to_have_text(text) | await expect(locator).to_have_text(text) |
| Timeout setting | page.set_default_timeout(15000) | page.set_default_timeout(15000) |
| Close | browser.close() | await browser.close() |

Locator construction and timeout configuration do not require await. Actions, navigation, browser creation, title retrieval, and async assertions do.

## Why these locators work

| Locator | Demo element |
|---|---|
| get_by_role("heading", name="todos", exact=True) | Main heading |
| get_by_placeholder("What needs to be done?") | New-todo textbox |
| get_by_test_id("todo-item") | Todo row |
| get_by_test_id("todo-title") | Todo text |
| get_by_test_id("todo-count") | Remaining-item counter |
| item.get_by_role("checkbox") | Checkbox within one todo row |
| get_by_role("link", name="Active", exact=True) | Active filter |
| get_by_role("textbox", name="Edit", exact=True) | Todo edit field after double-click |
| item.get_by_role("button", name="Delete", exact=True) | Delete button revealed by hovering |

`filter(has_text="...")` narrows a set of rows to the relevant task. Scoping a checkbox or button to its row avoids confusing it with controls elsewhere on the page.

## The ten lessons

1. Open the public page and check both its browser title and visible heading.
2. Fill the new-item textbox and press Enter. Check the added text and remaining count.
3. Add a task and check its checkbox. Verify both checked state and zero remaining tasks.
4. Add two tasks and complete one. Active shows the pending task, Completed shows the finished task, and All shows both.
5. Double-click the title to reveal Edit, replace the text, and press Enter to save.
6. Hover over the task so Delete becomes visible. Click it and assert there are zero rows.
7. Complete one of two tasks and click Clear completed. Verify only the unfinished task remains.
8. Add an item, wait for its localStorage persistence, reload, and verify it remains in the same browser context.

9. On Selenium’s public form, select Two in a dropdown and check/uncheck a checkbox.
10. Fill the public form with demo text, submit it, and verify the confirmation heading and message. This is an actual request to the practice endpoint.

## Why no conftest.py?

These are ordinary Python programs. Python calls main through the `if __name__ == "__main__"` entry point. They create and close resources explicitly. Pytest does not discover or inject any fixtures here. This lets you learn Playwright actions before adding a test framework.

## Waiting and cleanup

The runnable scripts use 15-second action/assertion timeouts and 45-second navigation timeouts. Auto-waiting and retrying assertions handle normal page readiness. Example 08 uses wait_for_function to check that persistence actually happened; it does not guess a sleep duration.

The `slow_mo` option in visible mode makes teaching actions easier to see. It is not the synchronization mechanism.

The browser closes in a finally block even if an assertion raises. The outer Playwright context manager then stops the driver. A failed script exits nonzero, and run_all.py retains that failure in its summary.
