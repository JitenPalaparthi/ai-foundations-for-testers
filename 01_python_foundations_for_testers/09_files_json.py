"""Files, paths, and JSON

Time: 7 minutes
Goal: Read structured test data safely.

Explanation:
Path(__file__) locates this script, and with_name finds the neighboring file regardless of the working directory. with closes the file automatically. json.load converts JSON arrays/objects into Python lists/dictionaries and JSON booleans into bool values. Summing booleans counts True values.

Expected result:
alice True; bob False; Active users: 1.

Try it:
Add another active user to users.json and rerun. Keep valid JSON: double quotes and lowercase true/false.
"""

import json
from pathlib import Path

print(Path(__file__).with_name("users.json"))

source = Path(__file__).with_name("users.json")
with source.open(encoding="utf-8") as handle:
    try:
        users = json.load(handle)
        print(type(users).__name__)
        userslist= users["users"]
        print(type(userslist).__name__)

        for user in userslist:
            print(user["username"], user["active"])

        print(f"Active users: {sum(user['active'] for user in userslist)}")

    except json.decoder.JSONDecodeError as e:
        print(e)

print("Other wise working")


#print(type(user['active'] for user in userslist))

## instead of users.json create users.yaml File
# User yamnl.load to load the yamnl file
