"""Modules and imports

Time: 7 minutes
Goal: Reuse a function from another example.

Explanation:
A Python file is a module. import_module loads the numbered teaching module and exposes its function as an attribute. Top-level statements run on first import, explaining the extra output. In production, put demonstrations under if __name__ == "__main__" to avoid import side effects.

Expected result:
The three demonstration results from example 06, then Imported check: True.

Try it:
Add a main guard to the three print calls in example 06; rerun this example and observe that only Imported check remains.
"""

from importlib import import_module

# Numeric teaching filenames cannot appear in a normal "from 06_..." statement.
# import_module accepts the module name as a string.
checks = import_module("06_functions")
print("Imported check:", checks.is_acceptable(200, 450))
print(checks.gen_fib(10))
