"""Select a dropdown option and change a checkbox.

Run: python async/09_dropdown.py
Headless: python async/09_dropdown.py --headless
Each run creates a fresh browser context and closes it afterward.
"""
import asyncio
import argparse
from playwright.async_api import async_playwright, expect

URL = "https://www.selenium.dev/selenium/web/web-form.html"


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
            dropdown = page.get_by_label("Dropdown (select)")
            await dropdown.select_option(label="Two")
            await expect(dropdown).to_have_value("2")
            checkbox = page.get_by_label("Default checkbox", exact=True)
            await checkbox.check()
            await expect(checkbox).to_be_checked()
            await checkbox.uncheck()
            await expect(checkbox).not_to_be_checked()

            print("PASS: 09_dropdown (async)")
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
