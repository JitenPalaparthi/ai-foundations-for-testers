"""Scope, filter, and locator chaining

Achieve: Click the correct button when several share a name.
Time: 6 minutes
Command: python -m pytest test_09_filter_scope.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
Both products have an Add to cart button. A page-wide click would violate strictness because it matches twice. Filter to one product, then find the button inside it. has_text matches descendant text as well.

Expected: Cart says Added Mouse.

Try it: Select Keyboard with filter(has=...).
"""

from playwright.sync_api import expect
def test_scoped_product(lab):
    card = lab.get_by_test_id("product-card").filter(has_text="Mouse")
    expect(card).to_have_count(1)
    card.get_by_role("button", name="Add to cart", exact=True).click()
    expect(lab.get_by_test_id("cart")).to_have_text("Added Mouse")
