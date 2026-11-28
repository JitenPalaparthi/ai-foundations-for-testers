"""New tabs and popups

Achieve: Capture the new page event before clicking.
Time: 6 minutes
Command: python -m pytest test_18_popup.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
expect_popup waits for a new page opened by this page. The context manager arms the listener before the click, then exposes the Page through value. Each tab has its own locators.

Expected: New help tab is verified and closed.

Try it: Assert the help paragraph.
"""

from playwright.sync_api import expect
def test_popup(lab):
    with lab.expect_popup() as popup_info:
       # lab.get_by_role("link", name="Open help", exact=True).click()
        lab.locator('a:has-text("Open help")').click()
    popup = popup_info.value
    expect(popup).to_have_title("Practice Help")
    expect(popup.get_by_role("heading", name="Practice Help", exact=True)).to_be_visible()
    popup.close()
