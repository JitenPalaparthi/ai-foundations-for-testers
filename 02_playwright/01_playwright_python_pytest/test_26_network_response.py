"""Observe a network response

Achieve: Wait for a specific request and verify UI plus payload.
Time: 8 minutes
Command: python -m pytest test_26_network_response.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
Arm expect_response before the click. Match the intended URL and method, inspect the response, then assert rendered content because receiving a response alone does not prove the UI used it correctly.

Expected: HTTP 200, payload Asha, and Asha rendered.

Try it: Assert the response content-type contains application/json.
"""

from playwright.sync_api import expect
def test_network_response(lab):
    with lab.expect_response(lambda response: response.url.endswith("/api/users") and response.request.method == "GET") as response_info:
        lab.get_by_role("button", name="Load users", exact=True).click()
    response = response_info.value
    assert response.status == 200
    assert response.json()["users"][0]["name"] == "Asha"
    expect(lab.locator("#users li")).to_have_text(["Asha"])
