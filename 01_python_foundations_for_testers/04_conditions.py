"""Conditions and boundaries

Time: 7 minutes
Goal: Translate an acceptance rule into decisions.

Explanation:
if/elif/else chooses the first matching branch. Indentation defines the block. <= includes the boundary 800, while < would exclude it. and requires both expressions to be true. != means not equal.

Expected result:
PASS, then True.

Try it:
Run response times 799, 800, and 801; predict the results before running.
"""

response_ms = 800
status_code = 200
if status_code != 200:
    outcome = "FAIL: unexpected status"
elif response_ms <= 800:
    outcome = "PASS"
else:
    outcome = "FAIL: too slow"
print(outcome)
print(status_code == 200 and response_ms <= 800)
# True and True
# True

ok = status_code == 200 and response_ms <= 800

if ok!=True:
    print("False")
else:
    print("True")
