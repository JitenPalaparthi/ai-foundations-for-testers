"""Confirm and prompt dialogs

Achieve: Register a handler before the dialog opens.
Time: 6 minutes
Command: python -m pytest test_16_dialogs.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
once registers a handler for one event. Dialog handlers must accept or dismiss; a handler that only logs leaves the action blocked. Register before clicking to avoid missing the event.

Expected: 2 tests pass per browser (4 total): confirmation accepted and prompt receives Asha.

Try it: Dismiss confirmation and assert Cancelled.
"""

from playwright.sync_api import expect
def test_confirm_accept(lab):
    lab.once("dialog", lambda dialog: dialog.accept())
    lab.get_by_role("button", name="Delete record", exact=True).click()
    expect(lab.locator("#delete-result")).to_have_text("Deleted")


def test_prompt(lab):
    lab.once("dialog", lambda dialog: dialog.accept("Asha"))
    lab.get_by_role("button", name="Enter display name", exact=True).click()
    expect(lab.locator("#display-name")).to_have_text("Hello Asha")
