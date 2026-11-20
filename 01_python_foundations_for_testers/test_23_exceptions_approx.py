"""pytest exceptions and floating-point checks

Time: 10 minutes
Goal: Verify error contracts and decimal calculations.

Explanation:
raises verifies that the enclosed operation throws the expected exception; match checks its message as a regular expression. A missing exception makes the test fail. Binary floating-point arithmetic can represent decimals approximately, so approx compares with a tolerance instead of requiring exact equality.

Expected result:
3 passed.

Try it:
Add a test accepting zero duration and a test for input "12.5".
"""

import pytest
from app_under_test import parse_duration


def test_invalid_duration():
    with pytest.raises(ValueError, match="numeric"):
        parse_duration("oops")


def test_negative_duration():
    with pytest.raises(ValueError, match="negative"):
        parse_duration("-1")


def test_decimal_sum():
    assert 0.1 + 0.2 == pytest.approx(0.3)
