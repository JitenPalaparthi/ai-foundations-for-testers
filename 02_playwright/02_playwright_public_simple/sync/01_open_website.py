"""Open a public website and check its title and heading.

Run: python sync/01_open_website.py
Headless: python sync/01_open_website.py --headless
Each run creates a fresh browser context and closes it afterward.
"""
import argparse
from playwright.sync_api import sync_playwright, expect

URL = "https://demo.playwright.dev/todomvc/"


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
            expect(page).to_have_title("React • TodoMVC")
            expect(page.get_by_role("heading", name="todos", exact=True)).to_be_visible()
            print("Website title:", page.title())

            print("PASS: 01_open_website (sync)")
        finally:
          browser.close()



if __name__ == "__main__":
    main()

# /html/body/section/div/header/input
