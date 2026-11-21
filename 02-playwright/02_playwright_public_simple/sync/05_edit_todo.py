"""Double-click an item, change its text, and save with Enter.

Run: python sync/05_edit_todo.py
Headless: python sync/05_edit_todo.py --headless
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
            entry.fill("Learn Python")
            entry.press("Enter")
            page.get_by_test_id("todo-title").dblclick()
            editor = page.get_by_role("textbox", name="Edit", exact=True)
            editor.fill("Learn Python and Playwright")
            editor.press("Enter")
            expect(page.get_by_test_id("todo-title")).to_have_text("Learn Python and Playwright")

            print("PASS: 05_edit_todo (sync)")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
