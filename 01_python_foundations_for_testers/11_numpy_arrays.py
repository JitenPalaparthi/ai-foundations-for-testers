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

list=[123,123.45,"Hello Worled",True,(10,12,11.23,True,"Hi")]
# [0x11,0x23,0x34,]
# Type, Address, some other medatadata
seconds = np.array([0.12, 0.25, 0.80, 1.20])
milliseconds = seconds * 1000
print(milliseconds)
print("Shape:", milliseconds.shape)
print("Dimensions:", milliseconds.ndim)

a = np.array([1,2,3,4,5])
b = np.array([10,9,8,7,6])
c = a+b
d = a*b
e = a ** b
print(a,b,c,d,e)

# a = [1,2,3,4,5]
# b = [10,9,8,7]
# c = a+b
# d = a*b
# e = a ** b
