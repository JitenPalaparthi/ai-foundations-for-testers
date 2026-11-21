"""Fill a public practice form and verify its confirmation.

Run: python sync/10_submit_form.py
Headless: python sync/10_submit_form.py --headless
Each run creates a fresh browser context and closes it afterward.
"""
import argparse
from playwright.sync_api import sync_playwright, expect

URL = "https://www.selenium.dev/selenium/web/web-form.html"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--headless", action="store_true", help="Run without a visible window")
    parser.add_argument("--chrome", action="store_true", help="Use installed Google Chrome")
    args = parser.parse_args()
    expect.set_options(timeout=15000)
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=args.headless,
            channel="chrome" if args.chrome else None,
            slow_mo=0 if args.headless else 200,
        )
        try:
            context = browser.new_context()
            page = context.new_page()
            page.set_default_timeout(15000)
            page.set_default_navigation_timeout(45000)

            page.goto(URL, wait_until="domcontentloaded")
            page.get_by_label("Text input", exact=True).fill("Playwright learner")
            page.get_by_label("Textarea", exact=True).fill("This is a public demo form.")
            page.get_by_role("button", name="Submit", exact=True).click()
            expect(page.get_by_role("heading", name="Form submitted", exact=True)).to_be_visible()
            expect(page.locator("#message")).to_have_text("Received!")

            print("PASS: 10_submit_form (sync)")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
