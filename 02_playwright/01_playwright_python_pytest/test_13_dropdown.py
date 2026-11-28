"""Native dropdowns

Achieve: Select by value, label, and index.
Time: 6 minutes
Command: python -m pytest test_13_dropdown.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
select_option works for native <select>. Value is the option value; label is the displayed text; index is zero-based including the placeholder. A custom dropdown built from divs requires clicking its visible controls instead.

Expected: Selections are IN, GB, then IN.

Try it: Save preferences and check the message.
"""

from playwright.sync_api import expect
def test_dropdown(lab):
    country = lab.get_by_label("Country", exact=True)
    country.select_option(value="IN")
    expect(country).to_have_value("IN")
    country.select_option(label="United Kingdom")
    expect(country).to_have_value("GB")
    country.select_option(index=1)
    expect(country).to_have_value("IN")
