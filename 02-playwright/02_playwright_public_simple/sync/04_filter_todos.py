"""Click links to show Active, Completed, and All items.

Run: python sync/04_filter_todos.py
Headless: python sync/04_filter_todos.py --headless
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
            entry = page.get_by_placeholder("What needs to be done?")
            entry.fill("Read a tutorial")
            entry.press("Enter")
            entry.fill("Write a test")
            entry.press("Enter")
            first = page.get_by_test_id("todo-item").filter(has_text="Read a tutorial")
            first.get_by_role("checkbox").check()
            page.get_by_role("link", name="Active", exact=True).click()
            expect(page.get_by_test_id("todo-title")).to_have_text(["Write a test"])
            page.get_by_role("link", name="Completed", exact=True).click()
            expect(page.get_by_test_id("todo-title")).to_have_text(["Read a tutorial"])
            page.get_by_role("link", name="All", exact=True).click()
            expect(page.get_by_test_id("todo-title")).to_have_text(["Read a tutorial", "Write a test"])

            print("PASS: 04_filter_todos (sync)")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
