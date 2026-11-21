"""pandas validation and export

Time: 9 minutes
Goal: Validate report structure and create a failure CSV.

Explanation:
Assertions express expected properties for a test or demonstration. isin validates allowed labels; ge checks a numeric lower bound and returns False for missing numeric values here. to_csv writes a table; index=False omits the pandas row index. A temporary directory keeps this demonstration repeatable and cleans up afterward. For production input validation use explicit exceptions because Python can disable assertions.

Expected result:
A failure table containing TC02 and TC05, followed by Exported failures: 2.

Try it:
Add a check that case_id is unique after deduplication. To retain the CSV, replace the temporary directory with a chosen output folder.
"""

from pathlib import Path
from tempfile import TemporaryDirectory
import pandas as pd

report = pd.read_csv(Path(__file__).with_name("test_results.csv")).drop_duplicates()
required = {"case_id", "status", "response_ms"}
assert required.issubset(report.columns), "Required columns are missing"
assert report["status"].isin(["PASS", "FAIL"]).all(), "Unknown status"
assert report["response_ms"].ge(0).all(), "Negative or missing response time"
failures = report.loc[report["status"].eq("FAIL")]
with TemporaryDirectory() as folder:
    output = Path("./") / "failures.csv"
    print(output)
    failures.to_csv(output, index=False)
    reloaded = pd.read_csv(output)
    print(reloaded.to_string(index=False))
    print("Exported failures:", len(reloaded))
