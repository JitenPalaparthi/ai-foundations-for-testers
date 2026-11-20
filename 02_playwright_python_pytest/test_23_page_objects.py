"""Page Object Model

Achieve: Move repeated selectors and actions into a reusable object.
Time: 8 minutes
Command: python -m pytest test_23_page_objects.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
LoginPage in pages.py groups login locators and the sign_in action. The test keeps its assertion so the business expectation stays visible. Avoid hiding every trivial locator behind unnecessary abstractions; refactor when reuse or change warrants it.

Expected: Login succeeds through the page object.

Try it: Use the same page object for an invalid login.
"""

from playwright.sync_api import expect
from pages import LoginPage


def test_page_object(lab):
    login = LoginPage(lab)
    login.sign_in("tester", "secret123")
    expect(login.message).to_have_text("Welcome, tester!")
