# Python Modules: Assignment

# 1. Investigate Circular Imports
# Fix the circular import problem between module_a.py and module_b.py. Resolve the circular dependency.
# module_a.py
def func_a():
    return "Function A"
def call_funcb():
    import b
    return b.func_b()
print(call_funcb())

# module_b.py
def func_b():
    return "Function B"
def call_funca():
    import a
    return a.func_a()

# 2. Dynamic Module Loading
# Write a program that dynamically imports and executes a function from any module specified by the user.
# Enter module name: math
# Enter function name: sqrt
# Enter argument: 25
# Output: 5.0
import importlib
module_name = input('Enter module name')
function_name = input('Enter function name')
argument = input('Enter argument')
# Convert argument to a number if possible (handle cases like integers or floats)
try:
    argument = float(argument) if '.' in argument else int(argument)
except ValueError:
    print("Invalid argument. Please enter a number.")
    exit()

try:
    module = importlib.import_module(module_name)
    func = getattr(module, function_name)
    result = func(argument)
    print(f"Output: {result}")

except ModuleNotFoundError:
    print(f"Module '{module_name}' not found.")
except AttributeError:
    print(f"Function '{function_name}' not found in module '{module_name}'.")
except Exception as e:
    print(f"Error: {e}")


# 3. Custom Module with Exception Handling
# Create a custom module calculator.py that handles division by zero and invalid inputs gracefully.
# calculator.py
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"Error: {e}"

import calculator
a = 33
b = 66
result = calculator.divide(a,b)
print(result)


# 4. Advanced Import Strategies
# Write a script that:
# Imports a module.
# Checks if a function exists.
# Executes it if available, otherwise gracefully handles the error.
import importlib
module_name = input('Enter module name')
function_name = input('Enter function name')
try:
    module = importlib.import_module(module_name)
    if hasattr(module, function_name):
        func = getattr(module, function_name)
        result = func()
        print(f"Output: {result}")
    else:
        print(f"Function '{function_name}' not found in module '{module_name}'.")
except ModuleNotFoundError:
    print(f"Module '{module_name}' not found.")
except Exception as e:
    print(f"Error: {e}")


# 5. Optimize Import Time
# Use time module to measure import time for different methods (single import vs. importing everything)
import time
start1 = time.time()
from math import sqrt
res = sqrt(25)
end1 = time.time()
print(f"Import time: {end1 - start1}")     #Single import(importing just a function from a module)

start2 = time.time()
import math
end2 = time.time()
print(f"Import time: {end2 - start2}")     #Importing entire module


# 6. Module Creation and Distribution
# Create a Python package structure with __init__.py.
# Write a setup.py to make it installable.
# Install your package locally.
# Import and test your package.
# module_a.py
def hello_from_a():
    return "Hello from module A"

# module_b.py
def hello_from_b():
    return "Hello from module B"

# __init__.py (makes the folder a package)
from .module_a import hello_from_a
from .module_b import hello_from_b

# setup.py (makes the package installable)
from setuptools import setup, find_packages

setup(
    name="my_package",  # Name of the package
    version="0.1",  # Version number
    packages=find_packages(),  # Automatically finds packages in the directory
    description="A sample Python package",  # Short description
    author="Your Name",  # Author information
    author_email="your.email@example.com",  # Author email
    classifiers=[
        "Programming Language :: Python :: 3",  # Compatible with Python 3
        "License :: OSI Approved :: MIT License",  # MIT License
        "Operating System :: OS Independent",  # Works on any OS
    ],
)

# To install the package locally, run:
# pip install .

# test_package.py (Test the package after installation)
import my_package
print(my_package.hello_from_a())  # Should print: Hello from module A
print(my_package.hello_from_b())  # Should print: Hello from module B


# 7. Investigate sys.path
# Explore sys.path and add a custom directory to import modules from an unconventional path
import sys
# Display the current sys.path, which contains the directories Python searches for modules
print("Original sys.path:", sys.path)
sys.path.append('/custom/path/to/modules')
import mymodule
# Test the module to ensure it works
print(mymodule.some_function())


# 8. Mocking Modules for Testing
# Write a unit test for a function that imports a module. Use unittest.mock to mock the imported module
import unittest
from unittest import mock
import math

class TestMathSqrt(unittest.TestCase):
    def test_mock_sqrt(self):
        # Mock math.sqrt to always return 100, regardless of the input
        with mock.patch('math.sqrt', return_value=100):
            result = math.sqrt(25)  # This would normally return 5, but it's mocked to return 100
            self.assertEqual(result, 100)  # Verify that the mock value is returned

if __name__ == '__main__':
    unittest.main()


# 9. Import Side Effects
# Investigate modules that run code at import time. Create a module that prints something as soon as it’s imported
# mymodule.py
print("This runs on import!")
import mymodule
# The statement in mymodule.py gets executed when we import the module, resulting in the message being printed to the terminal. 


# 10. Investigate Python’s Import Caching
# Explore sys.modules to understand how Python caches imports and how to reload modules
import sys
import mymodule
print(sys.modules['mymodule'])
# When import mymodule is called, Python loads the module and stores it in sys.modules.
# The print(sys.modules['mymodule']) statement will output the module object that's cached in sys.modules.
# This allows you to inspect the loaded module and verify that Python is using the cached version instead of reloading it every time. If we modify mymodule and want to reload it, you can use importlib.reload(mymodule).