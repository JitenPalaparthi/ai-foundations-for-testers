"""Double-click an item, change its text, and save with Enter.

Run: python async/05_edit_todo.py
Headless: python async/05_edit_todo.py --headless
Each run creates a fresh browser context and closes it afterward.
"""
import asyncio
import argparse
from playwright.async_api import async_playwright, expect

URL = "https://demo.playwright.dev/todomvc/"


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--headless", action="store_true", help="Run without a visible window")
    parser.add_argument("--chrome", action="store_true", help="Use installed Google Chrome")
    args = parser.parse_args()
    expect.set_options(timeout=15000)
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=args.headless,
            channel="chrome" if args.chrome else None,
            slow_mo=0 if args.headless else 200,
        )
        try:
            context = await browser.new_context()
            page = await context.new_page()
            page.set_default_timeout(15000)
            page.set_default_navigation_timeout(45000)

            await page.goto(URL, wait_until="domcontentloaded")
            entry = page.get_by_placeholder("What needs to be done?")
            await entry.fill("Learn Python")
            await entry.press("Enter")
            await page.get_by_test_id("todo-title").dblclick()
            editor = page.get_by_role("textbox", name="Edit", exact=True)
            await editor.fill("Learn Python and Playwright")
            await editor.press("Enter")
            await expect(page.get_by_test_id("todo-title")).to_have_text("Learn Python and Playwright")

            print("PASS: 05_edit_todo (async)")
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
