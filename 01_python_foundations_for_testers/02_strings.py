"""Strings and response checks

Time: 7 minutes
Goal: Inspect text returned by an application.

Explanation:
strip removes surrounding whitespace, lower normalizes case, in checks a substring, startswith checks a prefix, and split returns a list. Strings are immutable: these operations return new values. An f-string inserts values into readable output.

Expected result:
'login successful', True, True, ['tester', 'example.com'], then a formatted message.

Try it:
Check that the email ends with @example.com. Explain why lower() could hide a case-sensitivity defect.
"""

response = "  Login Successful  "
cleaned = response.strip().lower()
print(repr(cleaned))
print("successful" in cleaned)
print(cleaned.startswith("login"))
user = "tester@example.com"
print(user.split("@"))
print(f"User {user} received: {cleaned}")
