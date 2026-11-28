"""Small Page Object used by examples 23 and 30."""
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_label("Username", exact=True)
        self.password = page.get_by_label("Password", exact=True)
        self.submit = page.get_by_role("button", name="Sign in", exact=True)
        self.message = page.get_by_role("status")

    def sign_in(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()
