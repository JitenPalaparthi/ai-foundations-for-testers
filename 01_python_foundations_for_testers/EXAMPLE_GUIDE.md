# Example-by-example teaching guide

Run commands assume your terminal is in this directory with dependencies installed. Exercise answers are in EXERCISE_SOLUTIONS.md; show them after learners attempt the task.

## Variables, data types, and type conversion (7 minutes)

File: [01_variables_types.py](01_variables_types.py)

**Goal:** Represent test results and convert values from test data.

```sh
python 01_variables_types.py
```

**Walkthrough:** Variables bind names to values. str holds text, int holds whole numbers,
float holds floating-point numbers, bool holds True/False, and None represents
no value. type(value).__name__ gives the type name; == compares values.

Explicit conversion (often called type casting) uses int(), float(), str(),
or bool(). Converting a value returns a result; it does not change the original
variable unless you assign the result back. Python also converts an int to a
float automatically during mixed int/float arithmetic.

int(2.9) truncates toward zero; it does not round. int("2.9") and int("PASS")
raise ValueError because those strings are not valid integer text.
bool() checks truthiness: zero, empty strings, and None are false; nonempty
strings are true, including "False". Parse textual true/false values explicitly
and validate allowed values when reading real test data.

**Expected output:**

```text
Login with valid credentials
int float
Passed: True; error: None
True
Status conversion: 200 int | original: str
Response conversion: 0.42 float
Status for report: 200 str
Mixed arithmetic: 2.5 float
Truncated duration: 2
Truthiness: False True False False
Text flag: False
Invalid conversion: '2.9' is not integer text
```

**Learner exercise:** Change status_code to 404 and passed to False. Predict their types.
Convert "404" to int, "1.25" to float, and 500 to str; print each result and type.
Predict int(-2.9), bool("0"), and bool("") before trying them.

**Pacing:** Spend 2 minutes on basic types, 3 on conversions, 1 on the boolean/conversion pitfalls, and 1 on output predictions. Use the exercise as follow-up practice if needed.

## Strings and response checks (7 minutes)

File: [02_strings.py](02_strings.py)

**Goal:** Inspect text returned by an application.

```sh
python 02_strings.py
```

**Walkthrough:** strip removes surrounding whitespace, lower normalizes case, in checks a substring, startswith checks a prefix, and split returns a list. Strings are immutable: these operations return new values. An f-string inserts values into readable output.

**Expected result:** 'login successful', True, True, ['tester', 'example.com'], then a formatted message.

**Learner exercise:** Check that the email ends with @example.com. Explain why lower() could hide a case-sensitivity defect.

## Lists, tuples, sets, and dictionaries (7 minutes)

File: [03_collections.py](03_collections.py)

**Goal:** Choose collections for test data.

```sh
python 03_collections.py
```

**Walkthrough:** A list is ordered and mutable. A tuple is ordered and immutable. A set removes duplicates and has no guaranteed display order, so we sort it. A dictionary maps keys to values. Index 0 is first and -1 is last; get supplies a fallback for a missing key.

**Expected result:** 200 404; tester; [200, 404, 500]; login No error.

**Learner exercise:** Add a duration key to result and print it. Explain why a set cannot preserve repeated test runs.

## Conditions and boundaries (7 minutes)

File: [04_conditions.py](04_conditions.py)

**Goal:** Translate an acceptance rule into decisions.

```sh
python 04_conditions.py
```

**Walkthrough:** if/elif/else chooses the first matching branch. Indentation defines the block. <= includes the boundary 800, while < would exclude it. and requires both expressions to be true. != means not equal.

**Expected result:** PASS, then True.

**Learner exercise:** Run response times 799, 800, and 801; predict the results before running.

## Loops and test summaries (7 minutes)

File: [05_loops.py](05_loops.py)

**Goal:** Process a sequence of test outcomes.

```sh
python 05_loops.py
```

**Walkthrough:** for visits each item. enumerate adds a counter; start=1 makes it human-friendly. += increments the failure count. range excludes its stop value, so range(1, 4) produces three values.

**Expected result:** Four numbered cases, Failures: 1, and attempts 1, 2, 3.

**Learner exercise:** Count skipped cases separately. Explain why range(1, 3) produces only two attempts.

## Functions and reusable checks (7 minutes)

File: [06_functions.py](06_functions.py)

**Goal:** Write a reusable function with inputs and a return value.

```sh
python 06_functions.py
```

**Walkthrough:** def creates a function. Parameters receive caller inputs; limit_ms has a default. return sends a value back to the caller. Keyword arguments make optional settings readable. Keeping the check independent of printing makes it reusable in pytest.

**Expected result:** True, False, False.

**Learner exercise:** Call the function at exactly 800 ms. Change the default to 1000 and predict which calls change.

## Comprehensions and filtering (7 minutes)

File: [07_comprehensions.py](07_comprehensions.py)

**Goal:** Select failed and slow test cases.

```sh
python 07_comprehensions.py
```

**Walkthrough:** A list comprehension combines a loop, optional filter, and output expression. Each row is a dictionary. The if clause selects rows, and row["case"] extracts the field to keep. This is compact for simple transformations; use a normal loop when logic grows.

**Expected result:** ['checkout'] and ['checkout', 'search'].

**Learner exercise:** Build a list of durations for passing cases. Rewrite the failed comprehension as a for loop.

## Exceptions and invalid input (7 minutes)

File: [08_exceptions.py](08_exceptions.py)

**Goal:** Handle invalid values without hiding unexpected defects.

```sh
python 08_exceptions.py
```

**Walkthrough:** float can raise ValueError for nonnumeric text. raise explicitly rejects a domain-invalid value. try covers the operation that may fail; except ValueError handles only that expected failure type. The loop continues with the next input.

**Expected result:** 120.0, a conversion-error message for invalid, and Duration cannot be negative for -5.

**Learner exercise:** Add "0" to the inputs. Explain why a bare except could hide a programming error.

## Files, paths, and JSON (7 minutes)

File: [09_files_json.py](09_files_json.py)

**Goal:** Read structured test data safely.

```sh
python 09_files_json.py
```

**Walkthrough:** Path(__file__) locates this script, and with_name finds the neighboring file regardless of the working directory. with closes the file automatically. json.load converts JSON arrays/objects into Python lists/dictionaries and JSON booleans into bool values. Summing booleans counts True values.

**Expected result:** alice True; bob False; Active users: 1.

**Learner exercise:** Add another active user to users.json and rerun. Keep valid JSON: double quotes and lowercase true/false.

## Modules and imports (7 minutes)

File: [10_modules.py](10_modules.py)

**Goal:** Reuse a function from another example.

```sh
python 10_modules.py
```

**Walkthrough:** A Python file is a module. import_module loads the numbered teaching module and exposes its function as an attribute. Top-level statements run on first import, explaining the extra output. In production, put demonstrations under if __name__ == "__main__" to avoid import side effects.

**Expected result:** The three demonstration results from example 06, then Imported check: True.

**Learner exercise:** Add a main guard to the three print calls in example 06; rerun this example and observe that only Imported check remains.

## NumPy arrays and vectorized arithmetic (8 minutes)

File: [11_numpy_arrays.py](11_numpy_arrays.py)

**Goal:** Convert response times without a manual loop.

```sh
python 11_numpy_arrays.py
```

**Walkthrough:** A NumPy array stores a homogeneous sequence of values. Multiplication applies element by element, unlike Python list multiplication, which repeats a list. shape describes each axis length; ndim counts axes. np is the conventional import alias.

**Expected result:** [ 120.  250.  800. 1200.], Shape: (4,), Dimensions: 1.

**Learner exercise:** Compare [1, 2] * 3 with np.array([1, 2]) * 3.

## NumPy masks and SLA boundaries (9 minutes)

File: [12_numpy_filtering.py](12_numpy_filtering.py)

**Goal:** Find response times exceeding a limit.

```sh
python 12_numpy_filtering.py
```

**Walkthrough:** An array comparison creates a boolean mask with one value per element. Indexing with that mask selects matching elements. count_nonzero counts True values and all requires every value to be true. Exactly 800 ms is allowed by this acceptance rule.

**Expected result:** [False False False True], [1200], Slow count: 1, Within limit: False.

**Learner exercise:** Use >= instead of > and explain the change in the selected rows.

## NumPy statistics and percentiles (9 minutes)

File: [13_numpy_statistics.py](13_numpy_statistics.py)

**Goal:** Summarize performance measurements.

```sh
python 13_numpy_statistics.py
```

**Walkthrough:** The mean uses every value and responds to outliers. The median is the middle sorted value. NumPy uses linear interpolation by default for percentiles, so P95 need not equal an observed value. Five observations are only a teaching sample, not a reliable production latency estimate.

**Expected result:** Mean: 400.0; Median: 300.0; P95: 879.9999999999999 (approximately 880); Maximum: 1000.

**Learner exercise:** Replace 1000 with 10000 and compare how much the mean and median change.

## NumPy matrices and axes (9 minutes)

File: [14_numpy_matrix.py](14_numpy_matrix.py)

**Goal:** Compare response times across builds and endpoints.

```sh
python 14_numpy_matrix.py
```

**Walkthrough:** A two-dimensional array has rows and columns. [:, 2] selects every row in column index 2. axis=0 collapses the row axis, leaving one result per column. axis=1 collapses columns, leaving one result per row.

**Expected result:** Shape (2, 3); [100 200 300]; [300 500]; [125. 225. 400.]; [200. 300.].

**Learner exercise:** Calculate the maximum response per endpoint using axis=0.

## pandas CSV loading and inspection (9 minutes)

File: [15_pandas_read.py](15_pandas_read.py)

**Goal:** Load a test execution report.

```sh
python 15_pandas_read.py
```

**Walkthrough:** read_csv creates a DataFrame: a labeled table. shape returns row and column counts, columns contains labels, and dtypes shows inferred storage types. Inspecting input first helps catch missing columns or wrong numeric types before analysis.

**Expected result:** Six report rows; shape (6, 5); columns case_id, module, status, response_ms, owner. response_ms is numeric and owner contains a missing value.

**Learner exercise:** Print report.head(2) and report["status"].value_counts().

## pandas selection and filtering (9 minutes)

File: [16_pandas_filter.py](16_pandas_filter.py)

**Goal:** Extract failures and slow cases.

```sh
python 16_pandas_filter.py
```

**Walkthrough:** Selecting a column gives a Series. A comparison produces a boolean Series. loc selects rows and columns by labels or masks. Combine pandas conditions with & and parentheses around each condition; Python and does not perform elementwise combination.

**Expected result:** Failures TC02 (checkout) and TC05 (search); slow passing cases [TC04].

**Learner exercise:** Select checkout cases that failed or took longer than 800 ms. Use | for elementwise OR.

## pandas missing values and duplicates (9 minutes)

File: [17_pandas_missing.py](17_pandas_missing.py)

**Goal:** Identify incomplete and repeated records.

```sh
python 17_pandas_missing.py
```

**Walkthrough:** isna detects missing values, and summing its booleans counts them. duplicated marks repeated full rows after the first. drop_duplicates removes those repeats; copy makes an explicit independent table. fillna replaces missing labels. Only remove duplicates when repeated records are actually accidental.

**Expected result:** Missing owners: 1; Duplicate rows: 1; Clean rows: 5; TC04 has owner Unassigned.

**Learner exercise:** Compare drop_duplicates() with drop_duplicates(subset=["case_id"]). Explain why repeated executions might be legitimate.

## pandas grouping and report metrics (9 minutes)

File: [18_pandas_groupby.py](18_pandas_groupby.py)

**Goal:** Build a summary by application module.

```sh
python 18_pandas_groupby.py
```

**Walkthrough:** groupby partitions rows by module. Named aggregations define readable output columns. Boolean sum counts passes. Dividing passes by total produces the rate, and multiplying by 100 converts it to percent. Removing the accidental duplicate before aggregation prevents distorted results.

**Expected result:** checkout: total 2, passed 1, average 1050, pass rate 50%; login: 1, 1, 120, 100%; search: 2, 1, 400, 50%.

**Learner exercise:** Add maximum_ms=("response_ms", "max") to the aggregation.

## pandas validation and export (9 minutes)

File: [19_pandas_export.py](19_pandas_export.py)

**Goal:** Validate report structure and create a failure CSV.

```sh
python 19_pandas_export.py
```

**Walkthrough:** Assertions express expected properties for a test or demonstration. isin validates allowed labels; ge checks a numeric lower bound and returns False for missing numeric values here. to_csv writes a table; index=False omits the pandas row index. A temporary directory keeps this demonstration repeatable and cleans up afterward. For production input validation use explicit exceptions because Python can disable assertions.

**Expected result:** A failure table containing TC02 and TC05, followed by Exported failures: 2.

**Learner exercise:** Add a check that case_id is unique after deduplication. To retain the CSV, replace the temporary directory with a chosen output folder.

## pytest discovery and assertions (10 minutes)

File: [test_20_basic_assertions.py](test_20_basic_assertions.py)

**Goal:** Run passing tests and inspect one intentional failure.

```sh
python -m pytest test_20_basic_assertions.py -v
```

**Walkthrough:** pytest discovers test_*.py files and test_* functions. A test passes when execution finishes without an unhandled exception or failed assertion. pytest explains values in failing asserts. These toy checks teach syntax; later examples call application functions.

**Expected result:** 3 passed when run with python -m pytest test_20_basic_assertions.py -v.

**Learner exercise:** Temporarily change actual_status to 500, run the file, read the failure, and restore 200.

## pytest parameterized boundary cases (10 minutes)

File: [test_21_parametrize.py](test_21_parametrize.py)

**Goal:** Run one test against multiple inputs.

```sh
python -m pytest test_21_parametrize.py -v
```

**Walkthrough:** parametrize generates a separate test case for every input tuple. The argument names map values into function parameters. Testing below, at, and above a limit catches boundary errors. is compares bool singletons here; use == for general value equality.

**Expected result:** 4 passed; verbose output shows readable parameter IDs.

**Learner exercise:** Add (404, 800, False). Then mutate <= to < in app_under_test.py, observe the boundary failure, and restore it.

## pytest fixtures and isolated test data (10 minutes)

File: [test_22_fixtures.py](test_22_fixtures.py)

**Goal:** Share setup while keeping tests independent.

```sh
python -m pytest test_22_fixtures.py -v
```

**Walkthrough:** A fixture provides setup by matching its name to a test parameter. The default scope is function, so each test receives a new dictionary. Mutating the roles list in one test cannot affect another. Tests should never depend on execution order.

**Expected result:** 3 passed in any order.

**Learner exercise:** Add an email to the fixture and a test that checks its domain.

## pytest exceptions and floating-point checks (10 minutes)

File: [test_23_exceptions_approx.py](test_23_exceptions_approx.py)

**Goal:** Verify error contracts and decimal calculations.

```sh
python -m pytest test_23_exceptions_approx.py -v
```

**Walkthrough:** raises verifies that the enclosed operation throws the expected exception; match checks its message as a regular expression. A missing exception makes the test fail. Binary floating-point arithmetic can represent decimals approximately, so approx compares with a tolerance instead of requiring exact equality.

**Expected result:** 3 passed.

**Learner exercise:** Add a test accepting zero duration and a test for input "12.5".

## pytest files and dependency replacement (10 minutes)

File: [test_24_tmp_path_monkeypatch.py](test_24_tmp_path_monkeypatch.py)

**Goal:** Test file output and configuration without shared state.

```sh
python -m pytest test_24_tmp_path_monkeypatch.py -v
```

**Walkthrough:** tmp_path supplies a distinct temporary directory for each test. The file test verifies the observable saved content. monkeypatch changes environment variables for a test and restores them afterward. delenv with raising=False removes an optional setting safely. These tests exercise configuration, not network connectivity.

**Expected result:** 3 passed; no network requests are made.

**Learner exercise:** Save a result with passed=False and check its content. Explain why modifying a real shared result file would cause interference.

## Capstone: validate a report with pandas and pytest (15 minutes)

File: [test_25_report_capstone.py](test_25_report_capstone.py)

**Goal:** Combine fixtures, pandas transformations, and regression tests.

```sh
python -m pytest test_25_report_capstone.py -v
```

**Walkthrough:** StringIO provides an in-memory CSV, making the fixture self-contained. The first test verifies meaningful summary behavior, the second defines an empty-report policy, and the third guards against unintended mutation. approx handles the recurring decimal pass rate. The threshold includes all statuses: any response above 800 ms is slow.

**Expected result:** 3 passed. All six pytest files together initially produce 19 passed.

**Learner exercise:** Add a test with a response at exactly 800 ms and confirm it is not slow. Then add an all-failed report with a 0% pass rate.

