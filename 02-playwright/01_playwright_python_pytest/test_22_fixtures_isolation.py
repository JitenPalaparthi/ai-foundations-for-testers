"""Fixtures and browser isolation

Achieve: Reuse setup and prove storage starts clean.
Time: 8 minutes
Command: python -m pytest test_22_fixtures_isolation.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
conftest.py defines lab_url (session server), lab (function page navigation), and logged_in_page (function login). pytest resolves fixture dependencies. The page/context fixtures isolate cookies and storage per test even though the browser process may be shared. evaluate is used here only to inspect storage.

Expected: 2 passed per browser (4 total), independent of order.

Try it: Call Restore session in the fresh context and check its message.
"""

from playwright.sync_api import expect
def test_login_fixture(logged_in_page):
    expect(logged_in_page.get_by_role("status")).to_have_text("Welcome, tester!")
    assert logged_in_page.evaluate("localStorage.getItem('demo_user')") == "tester"


def test_fresh_context(lab):
    assert lab.evaluate("localStorage.getItem('demo_user')") is None
