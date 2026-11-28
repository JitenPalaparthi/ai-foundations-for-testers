"""Mock an API response

Achieve: Make the browser render controlled test data.
Time: 8 minutes
Command: python -m pytest test_27_mock_api.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
route intercepts matching requests; fulfill supplies a fake HTTP response. Register it before the action. This tests front-end rendering under controlled data; it does not validate the real backend. Use response observation or direct API tests for that.

Expected: UI renders Mock User instead of the real server value Asha.

Try it: Mock an empty users array and assert zero list items.
"""

from playwright.sync_api import expect
def test_mock_users(lab):
    lab.route("**/api/users", lambda route: route.fulfill(
        status=200, json={"users": [{"id": 99, "name": "Mock User"}]}))
    lab.get_by_role("button", name="Load users", exact=True).click()
    expect(lab.locator("#users li")).to_have_text(["Mock User"])
