"""First browser test

Achieve: Navigate to a page and verify its title and heading.
Time: 6 minutes
Command: python -m pytest test_01_first_test.py --browser chromium  --headed --slowmo 350

Explanation:
page is supplied by pytest-playwright. goto navigates. expect retries supported checks until they pass or time out. The page fixture owns browser-page cleanup.

Expected: 1 passed per browser (2 total); title and heading match.

Try it: Change the expected title and read the failure, then restore it.
"""

from playwright.sync_api import expect
import pytest

@pytest.mark.smoke
def test_homepage(page, lab_url):
    page.goto(lab_url)
    expect(page).to_have_title("Tester Practice Lab")
    expect(page.get_by_role("heading", name="Tester Practice Lab", exact=True)).to_be_visible()
