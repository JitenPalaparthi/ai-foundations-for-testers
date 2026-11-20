# Practice answers and trainer prompts

These are suggested answers. Apply edits one at a time, discuss the outcome, and restore deliberate defects before running the complete suite.

1. **Variables:** `status_code = 404` remains an `int`; `passed = False` remains a `bool`. Values change independently: Python does not automatically update `passed` when the status changes. `int("404")` gives `404` (int), `float("1.25")` gives `1.25` (float), and `str(500)` gives `"500"` (str). `int(-2.9)` gives `-2` because truncation is toward zero. `bool("0")` is True because the string is nonempty; `bool("")` is False.
2. **Strings:** `user.endswith("@example.com")` returns `True`. Lowercasing can hide defects when the specification requires exact case, so normalize only when the rule permits it.
3. **Collections:** `result["duration_ms"] = 420`; then `print(result["duration_ms"])`. A set merges equal values, losing execution frequency.
4. **Conditions:** 799 and 800 give PASS; 801 gives FAIL: too slow, provided the status remains 200.
5. **Loops:** Initialize `skipped = 0`, increment inside `if status == "SKIP":`, and print after the loop. `range(1, 3)` excludes 3, giving 1 and 2.
6. **Functions:** `is_acceptable(200, 800)` is True. Raising the default to 1000 does not change any of the three supplied calls: the explicit 500 limit still overrides the default. A new call at 900 changes from False to True.
7. **Comprehensions:** `[row["ms"] for row in results if row["status"] == "PASS"]` gives `[200, 850]`. The expanded failure selection is:

   ```python
   failed = []
   for row in results:
       if row["status"] == "FAIL":
           failed.append(row["case"])
   ```

8. **Exceptions:** Adding `"0"` prints `0.0`. A bare `except` also catches failures unrelated to the expected invalid input, making defects harder to detect.
9. **JSON:** Add `{"username": "carol", "active": true}` as a third array element, with a comma after the second element. Active users becomes 2.
10. **Modules:** Replace the three top-level print calls in example 06 with:

    ```python
    if __name__ == "__main__":
        print(is_acceptable(200, 600))
        print(is_acceptable(500, 100))
        print(is_acceptable(200, 600, limit_ms=500))
    ```

    Example 10 now prints only `Imported check: True`. Running example 06 directly still prints its three results.

11. **Arrays:** `[1, 2] * 3` gives `[1, 2, 1, 2, 1, 2]`; `np.array([1, 2]) * 3` gives `[3 6]`.
12. **Masks:** `response_ms >= 800` selects `[800 1200]`, so the slow count becomes 2. This changes the acceptance boundary.
13. **Statistics:** After replacing 1000 with 10000, the mean is 2200 and the median remains 300. The outlier affects the mean much more strongly.
14. **Axes:** `response_ms.max(axis=0)` gives `[150 250 500]`.
15. **Inspection:** `print(report.head(2))` displays TC01 and TC02. `print(report["status"].value_counts())` shows PASS 4 and FAIL 2, including the deliberate duplicate.
16. **Filtering:** `report.loc[(report["module"] == "checkout") & ((report["status"] == "FAIL") | (report["response_ms"] > 800))]` selects TC02 and TC04. Parentheses group the OR rule before combining it with the module rule.
17. **Cleaning:** Full-row deduplication removes only identical records. Deduplicating on `case_id` also removes later rows with a repeated ID even if their other fields differ. A retry or later build can legitimately reuse an ID, so use an execution ID or composite key when appropriate.
18. **Grouping:** Add `maximum_ms=("response_ms", "max"),` inside `agg`. Maximums are checkout 1200, login 120, search 600.
19. **Validation:** `assert report["case_id"].is_unique, "Repeated case ID"` passes after full-row deduplication for this sample. To retain output, write to `Path(__file__).with_name("failures.csv")` outside the temporary-directory block.
20. **First failure:** Setting `actual_status = 500` makes `test_success_status` fail with an assertion showing `500 == 200`. Restore 200 afterward.
21. **Parameters:** Add `(404, 800, False)` and a fifth ID such as `"not-found"`. Changing the implementation to `<` makes the at-limit case fail; restore `<=` afterward.
22. **Fixtures:** Add `"email": "alice@example.com"` to the fixture dictionary, then add:

    ```python
    def test_email_domain(user):
        assert user["email"].endswith("@example.com")
    ```

23. **Errors and decimals:** Add:

    ```python
    def test_zero_duration():
        assert parse_duration("0") == 0.0

    def test_decimal_duration():
        assert parse_duration("12.5") == pytest.approx(12.5)
    ```

24. **Temporary files:** In a new test accepting `tmp_path`, call `save_result(tmp_path / "failed.json", {"passed": False})`, load the file using `json.loads`, and assert its `passed` value `is False`. A shared output path can let one test overwrite another test's data.
25. **Capstone:** Add the following tests. The fixture is recreated for each function, so these edits stay isolated:

    ```python
    def test_exact_limit_is_not_slow(report):
        report.loc[report["case_id"].eq("TC02"), "response_ms"] = 800
        assert summarize_report(report)["slow_cases"] == ["TC03"]

    def test_all_failed(report):
        report["status"] = "FAIL"
        summary = summarize_report(report)
        assert summary["failed"] == 3
        assert summary["pass_rate_pct"] == 0.0
    ```
