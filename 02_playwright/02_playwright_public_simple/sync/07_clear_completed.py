"""Remove completed items while keeping an unfinished item.

Run: python sync/07_clear_completed.py
Headless: python sync/07_clear_completed.py --headless
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
            entry.fill("Finished task")
            entry.press("Enter")
            entry.fill("Pending task")
            entry.press("Enter")
            finished = page.get_by_test_id("todo-item").filter(has_text="Finished task")
            finished.get_by_role("checkbox").check()
            page.get_by_role("button", name="Clear completed", exact=True).click()
            expect(page.get_by_test_id("todo-title")).to_have_text(["Pending task"])

            print("PASS: 07_clear_completed (sync)")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
