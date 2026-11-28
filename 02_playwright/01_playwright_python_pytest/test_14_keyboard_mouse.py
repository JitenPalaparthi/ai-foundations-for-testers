"""Keyboard, hover, and double click

Achieve: Exercise event-driven interactions.
Time: 6 minutes
Command: python -m pytest test_14_keyboard_mouse.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
press sends a key to a locator, hover moves the pointer, and dblclick triggers a double-click event. fill sets a field efficiently; use press_sequentially when per-character keyboard events are the behavior under test.

Expected: Search result, hover hint, and double-click confirmation appear.

Try it: Replace fill with press_sequentially for the search input.
"""

from playwright.sync_api import expect
def test_keyboard_mouse(lab):
    search = lab.get_by_label("Search cases", exact=True)
    search.fill("checkout")
    search.press("Enter")
    expect(lab.locator("#search-result")).to_have_text("Searching: checkout")
    lab.get_by_title("Hover for help", exact=True).hover()
    expect(lab.get_by_text("Use stable locators", exact=True)).to_be_visible()
    lab.get_by_role("button", name="Double click me", exact=True).dblclick()
    expect(lab.locator("#double-result")).to_have_text("Double click received")
