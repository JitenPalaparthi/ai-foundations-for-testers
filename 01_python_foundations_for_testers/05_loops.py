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
import re

results = ["PASS", "FAIL", "PASS", "SKIP"]
failures = 0
for number, status in enumerate(results, start=1):
    print(f"Case {number}: {status}")
    if status == "FAIL":
        failures += 1

print(f"Failures: {failures}")

for attempt in range(1, 4):
    print(f"Attempt {attempt}")

for num in range(1,10):
    if num%2==0:
        print(num)

num =1
while num<=10:
    print(num)
    num+=1

a,b = 10,20
# t = b
# b = a
# print(t,a)
a,b = b,a # swap
print(a,b)

a,b = 0,1

for _ in range(1,11): # _ blank identifer
    print(a)
    a,b = b,a+b


# number=1
# for r in results:
#     print(f"Case {number}: {r}")
#     number+=1
