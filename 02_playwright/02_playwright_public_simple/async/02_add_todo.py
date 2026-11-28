"""Type in a textbox, press Enter, and verify the new item.

Run: python async/02_add_todo.py
Headless: python async/02_add_todo.py --headless
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
            await entry.fill("Learn Playwright")
            await entry.press("Enter")
            await expect(page.get_by_test_id("todo-title")).to_have_text("Learn Playwright")
            await expect(page.get_by_test_id("todo-count")).to_have_text("1 item left")

            print("PASS: 02_add_todo (async)")
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
