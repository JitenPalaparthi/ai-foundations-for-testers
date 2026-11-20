"""Label and placeholder

Achieve: Locate form fields using their visible meaning.
Time: 6 minutes
Command: python -m pytest test_06_label_placeholder.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
get_by_label uses associated label text, including for/id associations. get_by_placeholder uses the placeholder attribute. A placeholder is not a replacement for a proper accessible label.

Expected: Both fields contain expected values.

Try it: Fill the password using its label.
"""

from playwright.sync_api import expect
def test_label_and_placeholder(lab):
    lab.get_by_label("Username", exact=True).fill("tester")
    lab.get_by_placeholder("Write notes", exact=True).fill("Regression session")
    expect(lab.get_by_placeholder("Enter username", exact=True)).to_have_value("tester")
    expect(lab.get_by_label("Notes", exact=True)).to_have_value("Regression session")
