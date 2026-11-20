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
response  = "SignIn successfull"
line = "Hello World! \n How are you doing"
num = "200"
print(line)
print(repr(line))
cleaned = response.strip().lower()
print(repr(cleaned))
print("successful" in cleaned)
yes = "successful" in cleaned
print(cleaned.startswith("signin"))
user = "tester@example.com@info"
userlist = user.split("@")
print(user.split("@"))
print(type(userlist).__name__)
print(f"User {user} received: {cleaned}")

print(10+20-20)
print(10+20-20>5)
print(10+20-20>5 and 10>5)
print(10<<2)

# Arithmetic
# Logical
# Comparision
# Bitwise
