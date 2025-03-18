# Advanced Debugging Assignment

# 1. Error Classification
# Identify the type of error in the following code snippets and fix them
for i in range(5):                #Syntax error(missing colon)
    print(i)

x = 10 / 0

def calculate_area(radius):
    return 2 * 3.14 * radius

# 2. Debugging Complex Functions
# Debug the following function and correct the mistakes
def process_data(data):
    if len(data) == 0:
        return 0                 # Or any other default value you want for empty list
    total = 0
    for item in data:
        try:
            total += int(item)  
        except ValueError:
            continue             # Skip non-numeric values
    return total / len(data)
print(process_data(['10', '20', 'abc', '30']))  # Output: 20.0


# 3. Advanced Debugging Challenge
# You’re given a function that fails intermittently. Investigate the bug and fix it
import random
def unreliable_function():
    number = random.choice([0, 1, 2])
    try:
        return 10 / number                        #Zero division error
    except ZeroDivisionError:
        return "Can't divide by 0"

for i in range(10):
    print(unreliable_function())


# 4. Writing Debug-Friendly Code
# Refactor the following function to improve readability and add error handling
def calculate_discount(price, discount):
    try:
        # Ensure the price is a valid number
        price = float(price)
        
        # Handle discount as a percentage string or number
        if isinstance(discount, str):
            if discount.endswith('%'):
                discount = float(discount.strip('%'))  # Remove '%' and convert to float
            else:
                raise ValueError("Discount must be a percentage (e.g., '10%').")
        else:
            discount = float(discount)

        # Ensure discount is in a valid range (0 to 100%)
        if discount < 0 or discount > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")

        # Calculate the discount
        final_price = price - (price * discount / 100)
        return final_price

    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
print(calculate_discount(100, '10%'))  # Valid input
print(calculate_discount(100, 'abc'))  # Invalid discount
print(calculate_discount(100, '150%'))  # Discount out of range

# 5. Rubber Duck Debugging
# Explain the following code snippet step-by-step as if you’re teaching someone unfamiliar with coding
numbers = [1, 2, 3, 4, 5]           #numbers is a list of 5 elements
result = 1                          #variable result is assigned value 1
for num in numbers:                 #traversing through the list 'numbers'
    result *= num                   #each time result is multiplied with consecutive list elements
print("Product:", result)           #return final value of 'result'

# 6. Advanced Challenge: Debug a Multi-threaded Program
# Fix the race condition in the following code
import threading
counter = 0
counter_lock = threading.Lock()  # Create a Lock object

def increment():
    global counter
    for _ in range(100000):
        with counter_lock:  # Ensure exclusive access to the counter
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)       #Expected:20000

# 7. Activity: Debug with Breakpoints
# Learn to use breakpoints in your IDE (e.g., VSCode, PyCharm) to inspect variable states step-by-step
import pdb
def divide(a, b):
    result = a / b
    pdb.set_trace()     #breakpoint is triggered right after division
    return result
a = 10
b = 0
print(divide(a, b))
# (Pdb) p a  # Inspect the value of 'a'
# 10
# (Pdb) p b  # Inspect the value of 'b'
# 0
# (Pdb) n    # Step to the next line (this will raise a ZeroDivisionError)


# 8. Memory Leaks and Performance Debugging
# Optimize the following code and fix potential memory leaks
import time
def optimized_function():
    # Use generator expression to avoid storing the entire list in memory
    result = (i * 2 for i in range(100000))  # generator expression
    time.sleep(2)
    return result
# Since the result is a generator, we can use len() on it by converting to a list temporarily, or we can directly count the elements
print(sum(1 for _ in optimized_function()))  # Efficient count of elements in the generator


# 9. Unexpected None
# Debug why the function returns None
def add(a, b):
    return(a + b)
print(add(3, 4))                 #No return statement


# 10. Silent Failures
# Identify why the code doesn't raise an error
try:
    result = 10 / 0
except ZeroDivisionError:      #caught by the generic except clause, which then ignores it due to the pass
    pass
print("No error detected!")