"""Role and accessible name

Achieve: Locate controls as an assistive technology user would.
Time: 6 minutes
Command: python -m pytest test_05_role.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
get_by_role combines an implicit or explicit ARIA role with its accessible name. A native button already has role button. exact=True prevents partial name matching. Prefer meaningful user-facing locators when possible.

Expected: Named controls and heading are located.

Try it: Locate the Download report link by role.
"""

from playwright.sync_api import expect
def test_role(lab):
    expect(lab.get_by_role("button", name="Sign in", exact=True)).to_be_enabled()
    expect(lab.get_by_role("heading", name="Products", exact=True)).to_be_visible()
    expect(lab.get_by_role("link", name="Open help", exact=True)).to_have_attribute("target", "_blank")
