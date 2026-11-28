"""Markers, selection, and test organization

Achieve: Run a smoke subset or a named test.
Time: 8 minutes
Command: python -m pytest test_25_markers.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
Markers group tests independently of filenames. smoke is registered in pytest.ini. -m smoke selects marked tests; -k selects names; a node ID selects one specific function. Selection changes which tests run, not their behavior.

Expected: 2 passed per browser (4 total) for this file; -m smoke selects one per browser.

Try it: Run this file with -m smoke, then with -k table.
"""

from playwright.sync_api import expect
import pytest

@pytest.mark.smoke
def test_smoke_login_available(lab):
    expect(lab.get_by_role("button", name="Sign in", exact=True)).to_be_visible()


def test_table_available(lab):
    expect(lab.locator("#results-table tbody tr")).to_have_count(2)
