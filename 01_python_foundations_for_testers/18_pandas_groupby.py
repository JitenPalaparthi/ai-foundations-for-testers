"""pandas grouping and report metrics

Time: 9 minutes
Goal: Build a summary by application module.

Explanation:
groupby partitions rows by module. Named aggregations define readable output columns. Boolean sum counts passes. Dividing passes by total produces the rate, and multiplying by 100 converts it to percent. Removing the accidental duplicate before aggregation prevents distorted results.

Expected result:
checkout: total 2, passed 1, average 1050, pass rate 50%; login: 1, 1, 120, 100%; search: 2, 1, 400, 50%.

Try it:
Add maximum_ms=("response_ms", "max") to the aggregation.
"""

from pathlib import Path
import pandas as pd

report = pd.read_csv(Path(__file__).with_name("test_results.csv")).drop_duplicates()
report["passed"] = report["status"].eq("PASS")
summary = report.groupby("module").agg(
    total=("case_id", "count"),
    passed=("passed", "sum"),
    average_ms=("response_ms", "mean"),
)
summary["pass_rate_pct"] = summary["passed"] / summary["total"] * 100
print(summary.round(2).to_string())
