"""Fill a public practice form and verify its confirmation.

Run: python async/10_submit_form.py
Headless: python async/10_submit_form.py --headless
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
            await page.get_by_label("Text input", exact=True).fill("Playwright learner")
            await page.get_by_label("Textarea", exact=True).fill("This is a public demo form.")
            await page.get_by_role("button", name="Submit", exact=True).click()
            await expect(page.get_by_role("heading", name="Form submitted", exact=True)).to_be_visible()
            await expect(page.locator("#message")).to_have_text("Received!")

            print("PASS: 10_submit_form (async)")
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
