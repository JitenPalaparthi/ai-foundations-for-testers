"""Optional public website: TodoMVC

Achieve: Create, complete, and remove a todo item.
Time: 0 minutes (optional extension)
Command: python -m pytest test_32_public_todomvc.py --browser chromium --browser firefox -v --headed --slowmo 350 --run-public

Explanation:
This external demo provides a realistic mini-flow. Fresh contexts isolate local storage. Its DOM is controlled by another team and may change; keep it optional and verify it before class.

Expected: Todo is added, completed, and deleted; skipped by default.

Try it: Create a second todo and assert the two item texts.
"""

from playwright.sync_api import expect
import pytest

@pytest.mark.public
def test_public_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/")
    entry = page.get_by_placeholder("What needs to be done?")
    entry.fill("Prepare Playwright workshop")
    entry.press("Enter")
    todo = page.get_by_test_id("todo-item").filter(has_text="Prepare Playwright workshop")
    expect(todo).to_have_count(1)
    todo.get_by_role("checkbox").check()
    expect(todo).to_have_class("completed")
    todo.hover()
    todo.get_by_role("button", name="Delete", exact=True).click()
    expect(todo).to_have_count(0)
