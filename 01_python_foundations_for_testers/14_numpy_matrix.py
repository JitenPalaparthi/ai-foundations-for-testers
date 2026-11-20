"""NumPy matrices and axes

Time: 9 minutes
Goal: Compare response times across builds and endpoints.

Explanation:
A two-dimensional array has rows and columns. [:, 2] selects every row in column index 2. axis=0 collapses the row axis, leaving one result per column. axis=1 collapses columns, leaving one result per row.

Expected result:
Shape (2, 3); [100 200 300]; [300 500]; [125. 225. 400.]; [200. 300.].

Try it:
Calculate the maximum response per endpoint using axis=0.
"""

import numpy as np

# Rows are builds; columns are login, search, checkout.
response_ms = np.array([[100, 200, 300], [150, 250, 500]])
print("Shape:", response_ms.shape)
print("First build:", response_ms[0])
print("Checkout:", response_ms[:, 2])
print("Per endpoint:", response_ms.mean(axis=0))
print("Per build:", response_ms.mean(axis=1))
