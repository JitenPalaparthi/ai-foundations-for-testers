"""Text, alt text, and title

Achieve: Find messages, images, and tooltip metadata.
Time: 6 minutes
Command: python -m pytest test_07_text_alt_title.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
get_by_text matches text content, get_by_alt_text matches an alt attribute, and get_by_title matches a title attribute. A title locator does not check the document title; expect(page).to_have_title does.

Expected: Message, image, and save button are found.

Try it: Verify the page title and explain how that differs from get_by_title.
"""

from playwright.sync_api import expect
def test_text_alt_title(lab):
    expect(lab.get_by_text("Cart is empty", exact=True)).to_be_visible()
    expect(lab.get_by_alt_text("Testing academy logo", exact=True)).to_be_visible()
    expect(lab.get_by_title("Save preferences", exact=True)).to_have_text("Save")
