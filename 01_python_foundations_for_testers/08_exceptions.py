"""Exceptions and invalid input

Time: 7 minutes
Goal: Handle invalid values without hiding unexpected defects.

Explanation:
float can raise ValueError for nonnumeric text. raise explicitly rejects a domain-invalid value. try covers the operation that may fail; except ValueError handles only that expected failure type. The loop continues with the next input.

Expected result:
120.0, a conversion-error message for invalid, and Duration cannot be negative for -5.

Try it:
Add "0" to the inputs. Explain why a bare except could hide a programming error.
"""

def parse_duration(raw):
    duration = float(raw)
    if duration < 0:
        raise ValueError("Duration cannot be negative")
    return duration

for raw in ["120", "invalid", "-5"]:
    try:
        print(parse_duration(raw))
    except ValueError as error:
        print(f"Rejected {raw!r}: {error}")
