"""Click links to show Active, Completed, and All items.

Run: python async/04_filter_todos.py
Headless: python async/04_filter_todos.py --headless
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
            await entry.fill("Read a tutorial")
            await entry.press("Enter")
            await entry.fill("Write a test")
            await entry.press("Enter")
            first = page.get_by_test_id("todo-item").filter(has_text="Read a tutorial")
            await first.get_by_role("checkbox").check()
            await page.get_by_role("link", name="Active", exact=True).click()
            await expect(page.get_by_test_id("todo-title")).to_have_text(["Write a test"])
            await page.get_by_role("link", name="Completed", exact=True).click()
            await expect(page.get_by_test_id("todo-title")).to_have_text(["Read a tutorial"])
            await page.get_by_role("link", name="All", exact=True).click()
            await expect(page.get_by_test_id("todo-title")).to_have_text(["Read a tutorial", "Write a test"])

            print("PASS: 04_filter_todos (async)")
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
