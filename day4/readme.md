# Assignment Questions

1. **Define a sequence. What types of sequences exist in Python?**

   A sequence in Python is an ordered collection of elements that supports indexing, slicing, and iteration. Sequences allow you to access elements based on their position and can be of various types.

   Types of sequences in Python:
   - **Lists**: Mutable, ordered collection of items (e.g., [1, 2, 3]).
   - **Tuples**: Immutable, ordered collection of items (e.g., (1, 2, 3)).
   - **Strings**: Immutable sequence of characters (e.g., "hello").
   - **Ranges**: Immutable sequence of numbers, often used for iteration (e.g., range(5)).
   - **Bytes**: Immutable sequence of bytes (e.g., b'hello').
   - **Bytearrays**: Mutable sequence of bytes (e.g., bytearray(b'hello')).
   - **Memoryviews**: A view object that allows access to the internal data of other sequence types without copying (e.g., memoryview(b'hello')).

2. **Strings, lists, and tuples differ in:**

   - **Mutability**:
     - **Strings**: Immutable (can't be changed).
     - **Lists**: Mutable (can be changed).
     - **Tuples**: Immutable (can't be changed).

   - **Elements**:
     - **Strings**: Sequence of characters.
     - **Lists**: Can contain any type of elements.
     - **Tuples**: Can contain any type of elements.

   - **Use case**:
     - **Strings**: Represent text.
     - **Lists**: Ordered, changeable collections.
     - **Tuples**: Ordered, unchangeable collections.

   - **Example**:
     - String: "hello"
     - List: [1, 2, 3]
     - Tuple: (1, 2, 3)

3. **Indexing in Python allows you to access individual elements in a sequence (like a string, list, or tuple) by specifying their position.**

   - **Zero-based indexing**: The first element is at index 0, the second at index 1, and so on.

     Example:
     ```python
     my_list = [10, 20, 30, 40]
     print(my_list[0])  # Output: 10 (first element)
     print(my_list[2])  # Output: 30 (third element)
     ```

   - You can also use negative indexing to access elements from the end:
     ```python
     print(my_list[-1])  # Output: 40 (last element)
     print(my_list[-2])  # Output: 30 (second-to-last element)
     ```

---

## Problem-Solving Approach and Learnings

The following approaches were used to solve the given problems:

1. **Identifying the Longest Pipeline**: 
   The `max()` function was used to find the pipeline with the highest duration. Pipelines exceeding a specific threshold were then filtered using list comprehensions.

2. **Parsing Key-Value Pairs from a Configuration String**: 
   The string was split using the delimiter `=` for keys and values, and the `split()` method was employed to parse each pair into a list of tuples.

3. **Extracting Hashtags from a String**: 
   Regular expressions were used to identify patterns matching hashtags (`#\w+`), and `re.findall()` was used to extract all unique hashtags.

4. **Counting Keyword Occurrences**: 
   The string was split into words using the `split()` method, and the count of a specific keyword was determined using the `count()` method.

5. **Reversing a List of Transactions**: 
   List slicing (`[::-1]`) was utilized to reverse the order of transactions efficiently.

6. **Calculating the Average of Sensor Readings**: 
   The last 10 sensor readings were extracted using slicing, and the average was computed by summing the values and dividing by the total number of readings.

7. **Generating Usernames from Full Names**: 
   A combination of string splitting and indexing was used to generate usernames by taking the first letter of the first name and appending the full last name.

8. **Compressing Recurring Substrings**: 
   String slicing and division techniques were applied to identify recurring substrings and calculate their occurrences.

---

### Learnings and Insights:

The problems helped in understanding how to manipulate and process sequences such as lists, strings, and tuples effectively. Various Python techniques like list comprehensions, string methods, slicing, regular expressions, and built-in functions such as `max()`, `split()`, and `count()` were utilized to solve the tasks. These exercises reinforced the importance of efficient data manipulation, string parsing, and the ability to handle large datasets effectively. The approach to using Python’s built-in tools simplified complex problems, ensuring optimal and readable solutions.
