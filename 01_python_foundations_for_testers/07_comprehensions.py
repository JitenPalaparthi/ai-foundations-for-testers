"""Comprehensions and filtering

Time: 7 minutes
Goal: Select failed and slow test cases.

Explanation:
A list comprehension combines a loop, optional filter, and output expression. Each row is a dictionary. The if clause selects rows, and row["case"] extracts the field to keep. This is compact for simple transformations; use a normal loop when logic grows.

Expected result:
['checkout'] and ['checkout', 'search'].

Try it:
Build a list of durations for passing cases. Rewrite the failed comprehension as a for loop.
"""

results = [
    {"case": "login", "status": "PASS", "ms": 200},
    {"case": "checkout", "status": "FAIL", "ms": 950},
    {"case": "checkout", "status": "FAIL", "ms": 1024},
    {"case": "search", "status": "PASS", "ms": 850},
]
failed = [item["case"] for item in results if item["status"] == "FAIL"]
slow = [row["case"] for row in results if row["ms"] > 800]
print(failed)
print(slow)

f=[]
for row in results:
    if row["status"]=="FAIL":
        f.append(row["case"])

print("failed",f)

msg="Hello World!"

for c in msg:
    print(c)
