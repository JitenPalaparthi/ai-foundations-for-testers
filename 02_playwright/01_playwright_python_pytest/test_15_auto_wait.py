"""Auto-waiting and delayed UI

Achieve: Wait for behavior instead of sleeping.
Time: 6 minutes
Command: python -m pytest test_15_auto_wait.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
Actions wait for relevant actionability checks, such as visibility, stability, and enabled state. expect retries its condition. It does not magically know all background work; assert the specific completion signal. Avoid time.sleep and wait_for_timeout in normal tests.

Expected: The test passes after the delayed message appears.

Try it: Increase the site delay to 1000 ms; rerun without changing the test and restore the site.
"""

from playwright.sync_api import expect
def test_delayed_result(lab):
    lab.get_by_role("button", name="Load delayed result", exact=True).click()
    expect(lab.locator("#delayed-result")).to_have_text("Report ready", timeout=5000)
