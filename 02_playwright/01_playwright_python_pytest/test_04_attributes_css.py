"""Name, type, and attribute selectors

Achieve: Find elements by HTML attributes and CSS relationships.
Time: 6 minutes
Command: python -m pytest test_04_attributes_css.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
[name="username"] matches an exact attribute value. > selects direct children. ^= means starts with; *= means contains; $= means ends with. Name is an attribute selector, not a separate get_by_name method.

Expected: Correct username, password, and submit button are found.

Try it: Locate username with a placeholder ends-with selector.
"""

from playwright.sync_api import expect
def test_attribute_selectors(lab):
    lab.locator('input[name="username"]').fill("tester")
    lab.locator('input[type="password"]').fill("secret123")
    expect(lab.locator('#login-form > button[type="submit"]')).to_have_text("Sign in")
    expect(lab.locator('input[placeholder^="Enter"]')).to_have_count(1)
