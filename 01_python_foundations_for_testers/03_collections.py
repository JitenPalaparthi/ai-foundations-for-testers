"""Lists, tuples, sets, and dictionaries

Time: 7 minutes
Goal: Choose collections for test data.

Explanation:
A list is ordered and mutable. A tuple is ordered and immutable. A set removes duplicates and has no guaranteed display order, so we sort it. A dictionary maps keys to values. Index 0 is first and -1 is last; get supplies a fallback for a missing key.

Expected result:
200 404; tester; [200, 404, 500]; login No error.

Try it:
Add a duration key to result and print it. Explain why a set cannot preserve repeated test runs.
"""

statuses = [200, 500, 200]
statuses.append(404)
statuses.append(505)
credentials = ("tester", "demo-password")
unique_statuses = set(statuses)
anotherset = {10,20,20,30,40}; # set
result = {"case": "login", "passed": True,"age":43,"area":"Trivandrum"}
print(statuses[0], statuses[-1],statuses[4])
print(type(credentials).__name__,credentials[0])
print(sorted(unique_statuses))
print(result["case"], result.get("error", "No error"))

try:
    print(result["salary"])
except  KeyError:
    print("there is no associated value with the key salary")
    print("Check the tab")


try:
    num="number one"
    print(int(num))
except ValueError as e:
    print(e)




print("hello World")
