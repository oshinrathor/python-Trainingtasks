## 2.2. Values and Data Types
# Write a program that:
# Assigns different values to variables.
# Prints the type of each variable.
x = 42
y = 3.14
z = 'Hello'
print(type(x), type(y), type(z))

## 2.3. Operators and Operands
a = 10
b = 5
sum_result = a + b
print("Addition:", sum_result)

# Subtraction
sub_result = a - b
print("Subtraction:", sub_result)

# Multiplication
mul_result = a * b
print("Multiplication:", mul_result)

# Division
div_result = a / b
print("Division:", div_result)

# Comparison Operators
x = 8
y = 3
print("x > y:", x > y)   # Greater than
print("x < y:", x < y)   # Less than
print("x == y:", x == y) # Equal to
print("x != y:", x != y) # Not equal to

# Logical Operations
a = True
b = False

print("a and b:", a and b)  # True if both are True
print("a or b:", a or b)    # True if at least one is True
print("not a:", not a)      # Inverts the value of a

## 2.4. Function Calls
# Write a program that uses built-in functions inside expressions:
numbers = [5, 3, 8, 1]
print(max(numbers) - min(numbers))

### 2.4.2. Functions are Objects; Parentheses Invoke Functions
# Assign a function to a variable, then call the function using the new variable:
greet = print
greet('Hello, World!')


## 2.5. Data Types
# Create variables of different types and print their types:
a = 10
b = 'Python'
c = 3.14
print(type(a), type(b), type(c))

## 2.6. Type Conversion Functions
# Convert variables between types and observe the results:
num = '123'
converted_num = int(num)
print(converted_num, type(converted_num))   #result:123 <class 'int'>

## 2.7. Variables
#Assign values to variables, print them, and observe changes upon reassignment.
# Assign initial values
x = 10
y = 5

# Print initial values
print("Initial values:")
print("x =", x)
print("y =", y)

# Reassign values
x = 20
y = 15

# Print new values after reassignment
print("\nAfter reassignment:")
print("x =", x)
print("y =", y)

#Initial values:
x = 10
y = 5

# After reassignment:
x = 20
y = 15

## 2.8. Variable Names and Keywords
# Try using reserved keywords as variable names and observe the errors.
# Attempt to use reserved keywords as variable names
try:
    if = 10
except SyntaxError as e:
    print("Error:", e)

try:
    def = 5
except SyntaxError as e:
    print("Error:", e)

try:
    True = 20
except SyntaxError as e:
    print("Error:", e)
Error: invalid syntax
Error: invalid syntax
Error: cannot assign to keyword

## 2.9. Choosing the Right Variable Name
#Rewrite a piece of code with meaningful variable names.
a = 10
b = 5
c = a + b
print(c)
length = 10
width = 5
area = length + width
print(area)

## 2.10. Statements and Expressions
#Identify statements and expressions in this code:
x = 5 + 3
print(x)
Statement: x = 5 + 3, print(x)
Expression: 5 + 3

## 2.11. Order of Operations
#Write expressions using multiple operators to explore Python’s order of operations.
result = 2 + 3 * 4 ** 2 / 8
print(result)

## 2.12. Reassignment

### 2.12.1. Developing Your Mental Model of How Python Evaluates
#Assign a value to a variable, reassign it, and observe the changes:
count = 10
print(count)   #10
count = 20
print(count)    #20

## 2.13. Updating Variables
#Increment and decrement variables using `+=` and `-=`.
score = 100
score += 10
print(score)      #110
score -= 5
print(score)       #115