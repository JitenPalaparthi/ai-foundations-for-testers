"""Check a checkbox and verify its state.

Run: python sync/03_complete_todo.py
Headless: python sync/03_complete_todo.py --headless
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
            entry.fill("Read documentation")
            entry.press("Enter")
            item = page.get_by_test_id("todo-item")
            item.get_by_role("checkbox", name="Toggle Todo").check()
            expect(item.get_by_role("checkbox")).to_be_checked()
            expect(page.get_by_test_id("todo-count")).to_have_text("0 items left")

            print("PASS: 03_complete_todo (sync)")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
