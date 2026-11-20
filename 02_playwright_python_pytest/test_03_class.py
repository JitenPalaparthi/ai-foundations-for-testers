"""Locate by class

Achieve: Use one or multiple CSS classes.
Time: 6 minutes
Command: python -m pytest test_03_class.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
A dot selects a class. .text-input.user-field means one element with both classes; a space would mean a descendant. Class selectors can be brittle when styling classes change.

Expected: Field populated and 2 product cards found.

Try it: Select the sign-in button using its class.
"""

from playwright.sync_api import expect
def test_class(lab):
    field = lab.locator(".text-input.user-field")
    field.fill("class-demo")
    expect(field).to_have_value("class-demo")
    expect(lab.locator(".product-card")).to_have_count(2)
