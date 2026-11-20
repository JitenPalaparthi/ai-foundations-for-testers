"""Work inside an iframe

Achieve: Locate a control in a separate document.
Time: 6 minutes
Command: python -m pytest test_17_iframe.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
A normal page locator does not cross iframe document boundaries. frame_locator identifies the frame, then locators inside it find its content. Keep the frame selector stable and unique.

Expected: Ticket submitted appears inside the frame.

Try it: Assert the subject value before submitting.
"""

from playwright.sync_api import expect
def test_iframe(lab):
    support = lab.frame_locator('iframe[title="Support frame"]')
    support.get_by_label("Ticket subject", exact=True).fill("Login issue")
    support.get_by_role("button", name="Submit ticket", exact=True).click()
    expect(support.locator("#result")).to_have_text("Ticket submitted")
