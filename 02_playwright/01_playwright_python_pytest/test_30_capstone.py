"""Capstone user journey

Achieve: Combine login, preferences, product choice, and API output.
Time: 8 minutes
Command: python -m pytest test_30_capstone.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
The journey stitches individually taught actions into one readable flow. Assert milestones so failures point to a meaningful stage. Keep separate focused tests as well; a long journey should not replace all smaller checks.

Expected: Login, preferences, cart, and user list match their requirements.

Try it: Change the journey to select Mouse and United Kingdom.
"""

from playwright.sync_api import expect
from pages import LoginPage


def test_user_journey(lab):
    login = LoginPage(lab)
    login.sign_in("tester", "secret123")
    expect(login.message).to_have_text("Welcome, tester!")
    lab.get_by_label("Country", exact=True).select_option(label="India")
    lab.get_by_label("Accept terms", exact=True).check()
    lab.get_by_title("Save preferences", exact=True).click()
    expect(lab.locator("#saved")).to_have_text("Saved IN")
    card = lab.get_by_test_id("product-card").filter(has_text="Keyboard")
    card.get_by_role("button", name="Add to cart", exact=True).click()
    expect(lab.get_by_test_id("cart")).to_have_text("Added Keyboard")
    lab.get_by_role("button", name="Load users", exact=True).click()
    expect(lab.locator("#users li")).to_have_text(["Asha"])
