"""pandas selection and filtering

Time: 9 minutes
Goal: Extract failures and slow cases.

Explanation:
Selecting a column gives a Series. A comparison produces a boolean Series. loc selects rows and columns by labels or masks. Combine pandas conditions with & and parentheses around each condition; Python and does not perform elementwise combination.

Expected result:
Failures TC02 (checkout) and TC05 (search); slow passing cases [TC04].

Try it:
Select checkout cases that failed or took longer than 800 ms. Use | for elementwise OR.
"""

from pathlib import Path
import pandas as pd

report = pd.read_csv(Path(__file__).with_name("test_results.csv"))
failures = report.loc[report["status"] == "FAIL", ["case_id", "module"]]
slow_passes = report.loc[(report["status"] == "PASS") & (report["response_ms"] > 800)]
print(failures.to_string(index=False))
print("Slow passing cases:", slow_passes["case_id"].tolist())
