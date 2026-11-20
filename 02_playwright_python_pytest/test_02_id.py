"""Locate by ID

Achieve: Fill a uniquely identified field.
Time: 6 minutes
Command: python -m pytest test_02_id.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
CSS #username matches id="username". IDs should be unique. locator creates a reusable query; fill replaces current text.

Expected: Username contains tester.

Try it: Fill the password by ID.
"""

from playwright.sync_api import expect
def test_id(lab):
    field = lab.locator("#username")
    field.fill("tester")
    expect(field).to_have_value("tester")
