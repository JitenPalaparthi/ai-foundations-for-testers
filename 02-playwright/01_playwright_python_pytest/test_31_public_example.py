"""Optional public website: example.com

Achieve: Apply locators to an external page.
Time: 0 minutes (optional extension)
Command: python -m pytest test_31_public_example.py --browser chromium --browser firefox -v --headed --slowmo 350 --run-public

Explanation:
This opt-in example needs internet. A public site can change independently of the test. The local examples remain the reliable classroom path.

Expected: Public title and heading match; skipped unless --run-public is supplied.

Try it: Inspect the link by role without clicking it.
"""

from playwright.sync_api import expect
import pytest

@pytest.mark.public
def test_example_domain(page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
    expect(page.get_by_role("heading", name="Example Domain", exact=True)).to_be_visible()
