# Variables, Statements, and Expressions: A Learning Task

## Variables
A **variable** is a storage location in memory that holds a value.  
**Example:**
```python
x = 5
```

## Expressions
An **expression** is a combination of variables, values, and operators that evaluates to a result.  
**Example:**
```python
result = x + 3  # Evaluates to 8 if x = 5
```

## Statements
A **statement** is a line of code that performs an action, such as assigning a value or calling a function.  
**Example:**
```python
print("Hello, World!")
```

## Data Types
**Data types** specify what kind of value a variable can hold (e.g., integers, strings, lists).  
**Example:**
```python
x = 10  # integer
name = "Alice"  # string
```

## Type Conversions
**Type conversion** is the process of changing a value from one data type to another.  
**Example:**
```python
converted_value = int("123")  # Converts the string "123" to an integer
```

## Variable Naming Conventions
Python variable names should be descriptive, start with a letter or underscore, and avoid using reserved keywords.  
**Example:**
```python
my_variable = 10  # valid
# 1variable = 10    # invalid (this would cause an error)
```

## Flow of Execution
The **flow of execution** refers to the order in which the program executes statements, including function calls.  
**Example:**
```python
def greet(): 
    print("Hello!")  
greet()  # Function call
```

## Reassigning Variables
**Reassigning a variable** means updating its value during the program’s execution.  
**Example:**
```python
x = 5
x = x + 3  # x is now 8
```

---

## Python Values and Data Types

### What is a value in Python?
A **value** is data that a variable holds, such as numbers, text, or boolean values.

### Data Types in Python:
- **Integers**: Whole numbers.  
  **Example:** `x = 10`
  
- **Floats**: Numbers with decimal points.  
  **Example:** `y = 3.14`
  
- **Strings**: Text enclosed in quotes.  
  **Example:** `name = "Alice"`
  
- **Booleans**: Represents `True` or `False`.  
  **Example:** `is_active = True`

---

## Operators

### Arithmetic Operators:
- `+` (addition)
- `-` (subtraction)
- `*` (multiplication)
- `/` (division)
- `//` (floor division)
- `%` (modulus)
- `**` (exponentiation)

**Example:**
```python
x = 10 + 5
```

### Comparison Operators:
- `==` (equal)
- `!=` (not equal)
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal to)
- `<=` (less than or equal to)

**Example:**
```python
x > y
```

### Logical Operators:
- `and` (both True)
- `or` (at least one True)
- `not` (inverts)

**Example:**
```python
x > 5 and y < 10
```

---

## Python's Dynamic Typing
Python is **dynamically typed**, meaning you don’t need to declare variable types explicitly. The type is assigned at runtime based on the value.

**Example:**
```python
x = 10        # x is an integer
x = "Hello"   # Now x is a string
```

---

## Variable Naming: `total_price` vs `tp`

`total_price` is a better name than `tp` because it is more descriptive, improving code readability and maintainability. Clear, meaningful names make it easier to understand the purpose of a variable at a glance.

**Example:**
```python
total_price = 100  # Clearly represents the total price
tp = 100           # Less clear, could mean anything
```

---

## Statements vs Expressions

- **Statement**: A line of code that performs an action, such as assigning a value or calling a function.  
  **Example:**  
  ```python
  x = 10  # assignment statement
  ```

- **Expression**: A combination of variables, values, and operators that evaluates to a result.  
  **Example:**  
  ```python
  5 + 3  # evaluates to 8
  ```
