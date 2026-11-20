"""Data-driven login tests

Achieve: Run valid, invalid, and empty login inputs.
Time: 8 minutes
Command: python -m pytest test_21_parametrize.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
pytest creates one independent test for each row. Each case receives a fresh browser context through the default fixtures, so a successful login cannot leak into the next case. IDs explain which scenario failed.

Expected: 3 passed per browser (6 total).

Try it: Add an unknown user with the correct password.
"""

from playwright.sync_api import expect
import pytest

@pytest.mark.parametrize("username,password,message", [
    ("tester", "secret123", "Welcome, tester!"),
    ("tester", "wrong", "Invalid credentials"),
    ("", "", "Invalid credentials"),
], ids=["valid", "wrong-password", "empty"])
def test_login_cases(lab, username, password, message):
    lab.get_by_label("Username", exact=True).fill(username)
    lab.get_by_label("Password", exact=True).fill(password)
    lab.get_by_role("button", name="Sign in", exact=True).click()
    expect(lab.get_by_role("status")).to_have_text(message)
