"""Direct API testing

Achieve: Check an API without a page interaction.
Time: 8 minutes
Command: python -m pytest test_28_api_request.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
APIRequestContext sends HTTP directly. new_context(base_url=...) supports relative API paths. dispose releases resources. This contrasts with a page triggering fetch and is useful for API checks or test setup. Browser configuration flags do not configure this manually created API context.

Expected: API returns the expected JSON.

Try it: Check an unknown path returns HTTP 404.
"""

from playwright.sync_api import expect
def test_users_api(playwright, lab_url):
    api = playwright.request.new_context(base_url=lab_url)
    try:
        response = api.get("/api/users")
        assert response.ok
        assert response.status == 200
        assert response.json() == {"users": [{"id": 1, "name": "Asha"}]}
    finally:
        api.dispose()
