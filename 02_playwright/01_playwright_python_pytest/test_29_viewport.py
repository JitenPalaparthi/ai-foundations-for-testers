"""Viewport and browser configuration

Achieve: Exercise desktop and narrow layouts.
Time: 8 minutes
Command: python -m pytest test_29_viewport.py --browser chromium --browser firefox -v --headed --slowmo 350

Explanation:
set_viewport_size changes the viewport dimensions. A narrow viewport is not full device emulation: it does not set touch, user agent, or device scale. These viewport-only checks run on both Chromium and Firefox. Full mobile emulation is not supported on Firefox. This smoke check verifies core controls at two sizes, not a complete responsive-design audit.

Expected: 2 passed per browser (4 total) at desktop and narrow sizes.

Try it: Add a 768 by 1024 viewport case and run this file on both browsers.
"""

from playwright.sync_api import expect
import pytest

@pytest.mark.parametrize("width,height", [(1280, 720), (390, 844)], ids=["desktop", "narrow"])
def test_viewport(lab, width, height):
    lab.set_viewport_size({"width": width, "height": height})
    expect(lab.get_by_role("heading", name="Tester Practice Lab", exact=True)).to_be_visible()
    lab.get_by_label("Username", exact=True).fill("tester")
    expect(lab.get_by_label("Username", exact=True)).to_have_value("tester")
