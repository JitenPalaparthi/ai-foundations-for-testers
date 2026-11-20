"""Test IDs and XPath

Achieve: Compare explicit test contracts with structural selectors.
Time: 6 minutes
Command: python -m pytest test_08_testid_xpath.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
get_by_test_id defaults to data-testid and provides a deliberate testing contract. XPath selects by paths and predicates. Avoid absolute XPath tied to page layout; CSS/XPath structure can change during refactoring. XPath does not pierce shadow roots.

Expected: Test ID and XPath locate the intended controls.

Try it: Write an XPath for the username input.
"""

from playwright.sync_api import expect
def test_testid_and_xpath(lab):
    lab.get_by_test_id("username-input").fill("tester")
    expect(lab.locator('xpath=//form[@id="login-form"]//button[@type="submit"]')).to_have_text("Sign in")
    expect(lab.get_by_test_id("login-button")).to_have_count(1)
