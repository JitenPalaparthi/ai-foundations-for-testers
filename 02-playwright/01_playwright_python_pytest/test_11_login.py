"""Fill, click, and assert

Achieve: Automate a complete login outcome.
Time: 6 minutes
Command: python -m pytest test_11_login.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
Use Arrange (load via fixture), Act (fill and submit), Assert (verify visible outcome). Clicking alone does not prove login worked. These credentials belong only to this local teaching site.

Expected: Welcome, tester! is displayed.

Try it: Try a wrong password and assert the rejection message.
"""

from playwright.sync_api import expect
import pytest

@pytest.mark.smoke
def test_login(lab):
    lab.get_by_label("Username", exact=True).fill("tester")
    lab.get_by_label("Password", exact=True).fill("secret123")
    lab.get_by_role("button", name="Sign in", exact=True).click()
    expect(lab.get_by_role("status")).to_have_text("Welcome, tester!")
