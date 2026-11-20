"""pytest parameterized boundary cases

Time: 10 minutes
Goal: Run one test against multiple inputs.

Explanation:
parametrize generates a separate test case for every input tuple. The argument names map values into function parameters. Testing below, at, and above a limit catches boundary errors. is compares bool singletons here; use == for general value equality.

Expected result:
4 passed; verbose output shows readable parameter IDs.

Try it:
Add (404, 800, False). Then mutate <= to < in app_under_test.py, observe the boundary failure, and restore it.
"""

import pytest
from app_under_test import is_acceptable

@pytest.mark.parametrize("status, duration, expected", [
    (200, 799, True),
    (200, 800, True),
    (200, 801, False),
    (500, 100, False),
], ids=["below-limit", "at-limit", "above-limit", "bad-status"])
def test_acceptance_rule(status, duration, expected):
    assert is_acceptable(status, duration) is expected
