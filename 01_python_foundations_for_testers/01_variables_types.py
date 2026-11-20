"""Variables, data types, and type conversion

Time: 7 minutes
Goal: Represent test results and convert values from test data.

Explanation:
Variables bind names to values. str holds text, int holds whole numbers,
float holds floating-point numbers, bool holds True/False, and None represents
no value. type(value).__name__ gives the type name; == compares values.

Explicit conversion (often called type casting) uses int(), float(), str(),
or bool(). Converting a value returns a result; it does not change the original
variable unless you assign the result back. Python also converts an int to a
float automatically during mixed int/float arithmetic.

int(2.9) truncates toward zero; it does not round. int("2.9") and int("PASS")
raise ValueError because those strings are not valid integer text.
bool() checks truthiness: zero, empty strings, and None are false; nonempty
strings are true, including "False". Parse textual true/false values explicitly
and validate allowed values when reading real test data.

Expected result:
Login with valid credentials
int float
Passed: True; error: None
True
Status conversion: 200 int | original: str
Response conversion: 0.42 float
Status for report: 200 str
Mixed arithmetic: 2.5 float
Truncated duration: 2
Truthiness: False True False False
Text flag: False
Invalid conversion: '2.9' is not integer text

Try it:
Change status_code to 404 and passed to False. Predict their types.
Convert "404" to int, "1.25" to float, and 500 to str; print each result and type.
Predict int(-2.9), bool("0"), and bool("") before trying them.
"""

case_name = "Login with valid credentials"
status_code = 200
response_seconds = 0.42
passed = True
missing_error = None
num1 = 100

num2 = 123.432

ok = False
print(case_name)
print(type(ok))
ok= "Hello World!"
print(type(ok))
print(type(status_code).__name__, type(response_seconds).__name__)
print(f"Passed: {passed}; error: {missing_error}")
print(int("200") == status_code)

# 1. Text from a CSV or API -> integer for a numeric comparison.
raw_status = "200"
converted_status = int(raw_status)
print("Status conversion:", converted_status, type(converted_status).__name__,
      "| original:", type(raw_status).__name__)

# 2. Decimal text -> float for a response-time calculation.
raw_response = "0.42"
converted_response = float(raw_response)
print("Response conversion:", converted_response, type(converted_response).__name__)

# 3. Integer -> string for text-based reporting.
status_text = str(status_code)
print("Status for report:", status_text, type(status_text).__name__)

# 4. Implicit numeric conversion: int + float produces a float.
mixed_total = 2 + 0.5
print("Mixed arithmetic:", mixed_total, type(mixed_total).__name__)

# 5. Float -> integer removes the fractional part; this is not rounding.
print("Truncated duration:", int(2.9))

# 6. Boolean conversion checks whether a value is truthy.
print("Truthiness:", bool(0), bool("False"), bool(""), bool(None))
raw_flag = "False"
# This comparison parses a known true/false input; bool(raw_flag) would be True.
parsed_flag = raw_flag.strip().lower() == "true"
print("Text flag:", parsed_flag)

# 7. Invalid conversion: catch the expected error so the demo can finish.
# Exception handling is covered in detail in example 08.
try:
    int("2.9")
except ValueError:
    print("Invalid conversion: '2.9' is not integer text")

# Text Segment
# Data Segment
#
# Stack
# Heap
#
#


# 100    "Hello World"
# 0X11   0X45
# num1 -> 0x11
# name -> 0X45
