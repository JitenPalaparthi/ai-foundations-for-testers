"""NumPy masks and SLA boundaries

Time: 9 minutes
Goal: Find response times exceeding a limit.

Explanation:
An array comparison creates a boolean mask with one value per element. Indexing with that mask selects matching elements.
count_nonzero counts True values and all requires every value to be true.
Exactly 800 ms is allowed by this acceptance rule.

Expected result:
[False False False True], [1200], Slow count: 1, Within limit: False.

Try it:
Use >= instead of > and explain the change in the selected rows.
"""

import numpy as np

response_ms = np.array([120, 250, 800, 1200])
slow_mask = response_ms > 800
print(slow_mask)
print(response_ms[slow_mask])
print("Slow count:", np.count_nonzero(slow_mask))
print("Within limit:", np.all(response_ms <= 800))
