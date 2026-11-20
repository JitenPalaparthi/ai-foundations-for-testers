"""pandas CSV loading and inspection

Time: 9 minutes
Goal: Load a test execution report.

Explanation:
read_csv creates a DataFrame: a labeled table. shape returns row and column counts, columns contains labels, and dtypes shows inferred storage types. Inspecting input first helps catch missing columns or wrong numeric types before analysis.

Expected result:
Six report rows; shape (6, 5); columns case_id, module, status, response_ms, owner. response_ms is numeric and owner contains a missing value.

Try it:
Print report.head(2) and report["status"].value_counts().
"""

from pathlib import Path
import pandas as pd

report = pd.read_csv(Path(__file__).with_name("test_results.csv"))
print(report.to_string(index=False))
print("Shape:", report.shape)
print("Columns:", report.columns.tolist())
print(report.dtypes)
