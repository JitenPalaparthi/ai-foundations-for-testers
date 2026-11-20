"""Functions and reusable checks

Time: 7 minutes
Goal: Write a reusable function with inputs and a return value.

Explanation:
def creates a function. Parameters receive caller inputs; limit_ms has a default. return sends a value back to the caller. Keyword arguments make optional settings readable. Keeping the check independent of printing makes it reusable in pytest.

Expected result:
True, False, False.

Try it:
Call the function at exactly 800 ms. Change the default to 1000 and predict which calls change.
"""

def is_acceptable(status_code, response_ms, limit_ms=800):
    return status_code == 200 and response_ms <= limit_ms

print(is_acceptable(200, 600))
print(is_acceptable(500, 100))
print(is_acceptable(200, 600, limit_ms=500))
