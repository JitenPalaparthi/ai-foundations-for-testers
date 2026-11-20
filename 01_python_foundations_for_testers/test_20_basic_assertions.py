"""pytest discovery and assertions

Time: 10 minutes
Goal: Run passing tests and inspect one intentional failure.

Explanation:
pytest discovers test_*.py files and test_* functions. A test passes when execution finishes without an unhandled exception or failed assertion. pytest explains values in failing asserts. These toy checks teach syntax; later examples call application functions.

Expected result:
3 passed when run with python -m pytest test_20_basic_assertions.py -v.

Try it:
Temporarily change actual_status to 500, run the file, read the failure, and restore 200.
"""

def test_success_status():
    actual_status = 200
    assert actual_status == 200


def test_response_time_at_boundary():
    assert 800 <= 800


def test_login_message():
    assert "successful" in "Login successful".lower()
