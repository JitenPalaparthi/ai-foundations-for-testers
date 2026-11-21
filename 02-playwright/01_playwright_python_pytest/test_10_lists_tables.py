"""Lists, nth, and tables

Achieve: Assert repeated items and inspect a table row.
Time: 6 minutes
Command: python -m pytest test_10_lists_tables.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
nth uses zero-based indexing; first and last also exist. Prefer matching item identity when order is not a requirement. to_have_text with a list checks the texts and order of the matched elements.

Expected: Two products and two data rows; TC02 is FAIL.

Try it: Assert the first table case is PASS.
"""

from playwright.sync_api import expect
def test_lists_and_table(lab):
    cards = lab.get_by_test_id("product-card")
    expect(cards).to_have_count(2)
    expect(cards.nth(0).get_by_role("heading")).to_have_text("Keyboard")
    rows = lab.locator("#results-table tbody tr")
    expect(rows).to_have_count(2)
    failed_row = rows.filter(has_text="TC02")
    expect(failed_row.get_by_role("cell")).to_have_text(["TC02", "FAIL"])
