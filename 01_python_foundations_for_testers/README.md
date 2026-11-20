# 1. Python Foundations for Testers — 4 hours

Audience: testers new to Python. No previous Python knowledge assumed. This is a live workshop: introduce each concept, predict the output, run the example, explain it, and let learners attempt the exercise.

All examples are individual files in this directory. Every file includes its purpose, explanation, expected result, and a practice task in the opening docstring. `EXAMPLE_GUIDE.md` collects the same teaching notes for easy delivery.

## Setup before the session

Use Python 3.10 or newer for a fresh installation. A code editor and terminal are sufficient. No accounts, network APIs, or credentials are needed to run the examples after installing dependencies.

Open a terminal in this directory:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use `py -m venv .venv` and `.venv\Scripts\activate` in Command Prompt instead. Install dependencies before class; setup time is not part of the four hours. The dependency ranges allow compatible updates rather than locking every environment; see VALIDATION.md for the versions actually checked.

## Four-hour delivery plan

| Elapsed time | Topic | Delivery |
|---|---|---|
| 00:00–01:10 | Python basics | Examples 01–10, 7 minutes each |
| 01:10–01:15 | Break | 5 minutes |
| 01:15–01:50 | NumPy | Example 11: 8 minutes; 12–14: 9 minutes each |
| 01:50–02:35 | pandas | Examples 15–19, 9 minutes each |
| 02:35–02:40 | Break | 5 minutes |
| 02:40–03:45 | pytest | Examples 20–24: 10 minutes each; 25: 15 minutes |
| 03:45–04:00 | Review and questions | 15 minutes |

Total: 70 + 5 + 35 + 45 + 5 + 65 + 15 = **240 minutes**.

For a 7-minute example, spend 1 minute on the tester problem, 2 explaining the code, 1 predicting and running it, 2 on the exercise, and 1 reviewing. For a 9–10-minute example, allow more learner practice and discussion. For the 15-minute capstone, explain the contract for 3 minutes, run and inspect for 4, practice for 6, and review for 2. These are paced introductory demonstrations; advanced practice can continue after class.

## Running examples

```sh
python 01_variables_types.py
python 11_numpy_arrays.py
python 15_pandas_read.py
python -m pytest test_20_basic_assertions.py -v
python -m pytest -v
```

Run files 01–19 using Python, one at a time in numeric order. Run files 20–25 with pytest; running those files directly with Python only defines tests and does not execute them. `app_under_test.py` supplies functions for the tests. `users.json` and `test_results.csv` are local sample data. No example requires an external service.

Example 10 intentionally demonstrates import side effects from example 06. Example 19 writes and reads a temporary CSV that is removed automatically. The sample report contains an intentional duplicate row and a missing owner for cleaning exercises. Teaching exercises that temporarily introduce a defect must be restored before running the full suite.

Useful pytest commands:

```sh
python -m pytest -v                         # all 19 supplied test cases
python -m pytest test_21_parametrize.py -v   # one example
python -m pytest -k boundary -v             # match a test name
python -m pytest -x                         # stop at first failure
python -m pytest --junitxml=results.xml      # create a CI-readable report
```

## Trainer checklist

Before class, install dependencies and run all examples plus the test suite. During class, ask learners to predict an output before executing each example. Explain indentation, zero-based indexing, and the difference between assignment (`=`) and comparison (`==`) early. Revisit the same rule throughout: status 200 and response time at most 800 ms is acceptable.

Use the final 15 minutes to ask learners to explain a list versus a NumPy array versus a DataFrame, change a boundary, interpret an assertion failure, and describe fixture isolation. A learner has met the session goal when they can read a CSV, select failures, calculate a simple summary, and run a parameterized pytest test.

## Example index

| File | Topic | Minutes |
|---|---|---:|
| [01_variables_types.py](01_variables_types.py) | Variables, data types, and type conversion | 7 |
| [02_strings.py](02_strings.py) | Strings and response checks | 7 |
| [03_collections.py](03_collections.py) | Lists, tuples, sets, and dictionaries | 7 |
| [04_conditions.py](04_conditions.py) | Conditions and boundaries | 7 |
| [05_loops.py](05_loops.py) | Loops and test summaries | 7 |
| [06_functions.py](06_functions.py) | Functions and reusable checks | 7 |
| [07_comprehensions.py](07_comprehensions.py) | Comprehensions and filtering | 7 |
| [08_exceptions.py](08_exceptions.py) | Exceptions and invalid input | 7 |
| [09_files_json.py](09_files_json.py) | Files, paths, and JSON | 7 |
| [10_modules.py](10_modules.py) | Modules and imports | 7 |
| [11_numpy_arrays.py](11_numpy_arrays.py) | NumPy arrays and vectorized arithmetic | 8 |
| [12_numpy_filtering.py](12_numpy_filtering.py) | NumPy masks and SLA boundaries | 9 |
| [13_numpy_statistics.py](13_numpy_statistics.py) | NumPy statistics and percentiles | 9 |
| [14_numpy_matrix.py](14_numpy_matrix.py) | NumPy matrices and axes | 9 |
| [15_pandas_read.py](15_pandas_read.py) | pandas CSV loading and inspection | 9 |
| [16_pandas_filter.py](16_pandas_filter.py) | pandas selection and filtering | 9 |
| [17_pandas_missing.py](17_pandas_missing.py) | pandas missing values and duplicates | 9 |
| [18_pandas_groupby.py](18_pandas_groupby.py) | pandas grouping and report metrics | 9 |
| [19_pandas_export.py](19_pandas_export.py) | pandas validation and export | 9 |
| [test_20_basic_assertions.py](test_20_basic_assertions.py) | pytest discovery and assertions | 10 |
| [test_21_parametrize.py](test_21_parametrize.py) | pytest parameterized boundary cases | 10 |
| [test_22_fixtures.py](test_22_fixtures.py) | pytest fixtures and isolated test data | 10 |
| [test_23_exceptions_approx.py](test_23_exceptions_approx.py) | pytest exceptions and floating-point checks | 10 |
| [test_24_tmp_path_monkeypatch.py](test_24_tmp_path_monkeypatch.py) | pytest files and dependency replacement | 10 |
| [test_25_report_capstone.py](test_25_report_capstone.py) | Capstone: validate a report with pandas and pytest | 15 |
