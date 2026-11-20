"""NumPy arrays and vectorized arithmetic

Time: 8 minutes
Goal: Convert response times without a manual loop.

Explanation:
A NumPy array stores a homogeneous sequence of values. Multiplication applies element by element, unlike Python list multiplication, which repeats a list. shape describes each axis length; ndim counts axes. np is the conventional import alias.

Expected result:
[ 120.  250.  800. 1200.], Shape: (4,), Dimensions: 1.

Try it:
Compare [1, 2] * 3 with np.array([1, 2]) * 3.
"""

import numpy as np

seconds = np.array([0.12, 0.25, 0.80, 1.20])
milliseconds = seconds * 1000
print(milliseconds)
print("Shape:", milliseconds.shape)
print("Dimensions:", milliseconds.ndim)
