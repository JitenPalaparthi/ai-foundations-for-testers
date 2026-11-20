"""Capstone: validate a report with pandas and pytest

Time: 15 minutes
Goal: Combine fixtures, pandas transformations, and regression tests.

Explanation:
StringIO provides an in-memory CSV, making the fixture self-contained. The first test verifies meaningful summary behavior, the second defines an empty-report policy, and the third guards against unintended mutation. approx handles the recurring decimal pass rate. The threshold includes all statuses: any response above 800 ms is slow.

Expected result:
3 passed. All six pytest files together initially produce 19 passed.

Try it:
Add a test with a response at exactly 800 ms and confirm it is not slow. Then add an all-failed report with a 0% pass rate.
"""

from io import StringIO
import pandas as pd
import pytest
from app_under_test import summarize_report

@pytest.fixture
def report():
    return pd.read_csv(StringIO(
        "case_id,module,status,response_ms\n"
        "TC01,login,PASS,120\n"
        "TC02,checkout,FAIL,1200\n"
        "TC03,checkout,PASS,900\n"
    ))


def test_summary_counts_and_rate(report):
    summary = summarize_report(report)
    assert summary["total"] == 3
    assert summary["failed"] == 1
    assert summary["pass_rate_pct"] == pytest.approx(200 / 3)
    assert summary["slow_cases"] == ["TC02", "TC03"]


def test_empty_report(report):
    summary = summarize_report(report.iloc[0:0])
    assert summary == {"total": 0, "failed": 0, "pass_rate_pct": 0.0, "slow_cases": []}


def test_does_not_modify_input(report):
    before = report.copy(deep=True)
    summarize_report(report)
    pd.testing.assert_frame_equal(report, before)
