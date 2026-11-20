"""Assertions and screenshots

Achieve: Verify text, values, state, attributes, URL, and evidence.
Time: 6 minutes
Command: python -m pytest test_20_assertions_screenshots.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
Use web-first expect for dynamic browser state. Ordinary assert suits already returned Python values such as file sizes. A screenshot is evidence, not a visual regression assertion by itself. The URL assertion compares navigation against the independently expected lab address.

Expected: Browser properties match and a nonempty PNG is saved to tmp_path.

Try it: Navigate to the Login section link and assert the URL ends in #login.
"""

from playwright.sync_api import expect
def test_assertions_and_screenshot(lab, lab_url, tmp_path):
    expect(lab).to_have_url(lab_url + "/")
    expect(lab.locator("#username")).to_be_empty()
    expect(lab.locator("#password")).to_have_attribute("type", "password")
    expect(lab.get_by_role("button", name="Sign in", exact=True)).to_be_enabled()
    expect(lab.locator("#delayed-result")).to_be_empty()
    destination = tmp_path / "homepage.png"
    lab.screenshot(path=str(destination), full_page=True)
    assert destination.stat().st_size > 0
