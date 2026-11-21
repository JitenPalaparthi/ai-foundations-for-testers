"""Checkboxes and radio buttons

Achieve: Set and verify state deterministically.
Time: 6 minutes
Command: python -m pytest test_12_checkbox_radio.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
check/uncheck set a desired state instead of blindly toggling it. Radios in the same name group are mutually exclusive. Assertions verify the resulting state.

Expected: Terms end unchecked and Pro plan selected.

Try it: Use set_checked(True) for terms.
"""

from playwright.sync_api import expect
def test_checkbox_radio(lab):
    terms = lab.get_by_label("Accept terms", exact=True)
    terms.check()
    expect(terms).to_be_checked()
    terms.uncheck()
    expect(terms).not_to_be_checked()
    lab.get_by_label("Pro plan", exact=True).check()
    expect(lab.get_by_label("Pro plan", exact=True)).to_be_checked()
    expect(lab.get_by_label("Basic plan", exact=True)).not_to_be_checked()
