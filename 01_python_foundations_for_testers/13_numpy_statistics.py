"""NumPy statistics and percentiles

Time: 9 minutes
Goal: Summarize performance measurements.

Explanation:
The mean uses every value and responds to outliers. The median is the middle sorted value. NumPy uses linear interpolation by default for percentiles, so P95 need not equal an observed value. Five observations are only a teaching sample, not a reliable production latency estimate.

Expected result:
Mean: 400.0; Median: 300.0; P95: 879.9999999999999 (approximately 880); Maximum: 1000.

Try it:
Replace 1000 with 10000 and compare how much the mean and median change.
"""

import numpy as np

response_ms = np.array([100, 200, 300, 400,800, 900,1000])
print("Mean:", np.mean(response_ms))
print("Median:", np.median(response_ms))
print("Mode:", np.mode(response_ms))
print("P50:", np.percentile(response_ms, 50))
print("Maximum:", np.max(response_ms))
