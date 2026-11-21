"""Reload and verify the same browser context keeps saved items.

Run: python sync/08_reload_persistence.py
Headless: python sync/08_reload_persistence.py --headless
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
            entry.fill("Remember this task")
            entry.press("Enter")
            expect(page.get_by_test_id("todo-title")).to_have_text("Remember this task")
            # Wait for the app to persist the item before reloading.
            page.wait_for_function("() => JSON.parse(localStorage.getItem('react-todos') || '[]').length === 1")
            page.reload(wait_until="domcontentloaded")
            expect(page.get_by_test_id("todo-title")).to_have_text("Remember this task")

            print("PASS: 08_reload_persistence (sync)")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
