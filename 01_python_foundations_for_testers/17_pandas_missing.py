"""pandas missing values and duplicates

Time: 9 minutes
Goal: Identify incomplete and repeated records.

Explanation:
isna detects missing values, and summing its booleans counts them. duplicated marks repeated full rows after the first. drop_duplicates removes those repeats; copy makes an explicit independent table. fillna replaces missing labels. Only remove duplicates when repeated records are actually accidental.

Expected result:
Missing owners: 1; Duplicate rows: 1; Clean rows: 5; TC04 has owner Unassigned.

Try it:
Compare drop_duplicates() with drop_duplicates(subset=["case_id"]). Explain why repeated executions might be legitimate.
"""

from pathlib import Path
import pandas as pd

report = pd.read_csv(Path(__file__).with_name("test_results.csv"))
print("Missing owners:", report["owner"].isna().sum())
print("Duplicate rows:", report.duplicated().sum())
clean = report.drop_duplicates().copy()
clean["owner"] = clean["owner"].fillna("Unassigned")
print("Clean rows:", len(clean))
print(clean[["case_id", "owner"]].to_string(index=False))
