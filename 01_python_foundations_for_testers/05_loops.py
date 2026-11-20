"""Loops and test summaries

Time: 7 minutes
Goal: Process a sequence of test outcomes.

Explanation:
for visits each item. enumerate adds a counter; start=1 makes it human-friendly. += increments the failure count. range excludes its stop value, so range(1, 4) produces three values.

Expected result:
Four numbered cases, Failures: 1, and attempts 1, 2, 3.

Try it:
Count skipped cases separately. Explain why range(1, 3) produces only two attempts.
"""

results = ["PASS", "FAIL", "PASS", "SKIP"]
failures = 0
for number, status in enumerate(results, start=1):
    print(f"Case {number}: {status}")
    if status == "FAIL":
        failures += 1
print(f"Failures: {failures}")
for attempt in range(1, 4):
    print(f"Attempt {attempt}")
