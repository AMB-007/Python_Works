# ==============================================================================
#                  PYTHON TECHNICAL INTERVIEW QUESTIONS & ANSWERS
# ==============================================================================
# A comprehensive, single-file technical Q&A reference guide covering all topics 
# in Python programming — from core basics to advanced collection operations,
# functions, algorithms, and technical interview concepts.
# ==============================================================================


# ==============================================================================
# SECTION 1: PYTHON BASICS, I/O, VARIABLES & OPERATORS
# ==============================================================================

"""
Q1: What are the fundamental built-in data types in Python?
A: Python's core data types include:
   - Numeric: int, float, complex
   - Sequence: str, list, tuple
   - Mapping: dict
   - Set Types: set, frozenset
   - Boolean: bool (True, False)
   - Binary: bytes, bytearray, memoryview
   - None Type: NoneType (None)

Q2: What is the difference between `/` (float division) and `//` (floor division)?
A: 
   - `/` performs standard division and ALWAYS returns a float.
     Example: 5 / 2 -> 2.5
   - `//` performs floor division and rounds DOWN to the nearest integer.
     Example: 5 // 2 -> 2; -5 // 2 -> -3

Q3: What does the `%` (modulus) operator do, and how is it used in logic building?
A: The modulus operator returns the remainder of a division.
   Common uses:
   1. Checking Even/Odd: `n % 2 == 0`
   2. Extracting the last digit of a number: `last_digit = n % 10`
   3. Cyclical indexing or checking divisibility: `n % k == 0`

Q4: What is type casting in Python? Differentiate Implicit vs Explicit type casting.
A: 
   - Implicit Casting: Done automatically by Python interpreter.
     Example: 5 + 2.5 -> 7.5 (int implicitly converted to float).
   - Explicit Casting: Manually converting using built-in functions:
     int("10"), float(5), str(100), list((1, 2, 3)).

Q5: Why does `input()` always return a string, and how do you handle numerical inputs?
A: `input()` reads data from stdin as raw text. To do numerical calculations, you 
   must explicitly cast it:
   age = int(input("Enter age: "))
   price = float(input("Enter price: "))
"""

# Code Demonstration - Basics & Operators
def demo_basics():
    # Floor division vs Float division
    print("5 / 2 =", 5 / 2)      # 2.5
    print("5 // 2 =", 5 // 2)    # 2
    print("-5 // 2 =", -5 // 2)  # -3

    # Swap without temporary variable
    a, b = 10, 20
    a, b = b, a
    print(f"Swapped: a={a}, b={b}")

    # Bitwise XOR swap logic
    x, y = 5, 9
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print(f"XOR Swapped: x={x}, y={y}")


# ==============================================================================
# SECTION 2: DECISION MAKING & CONTROL FLOW
# ==============================================================================

"""
Q6: How does short-circuit evaluation work with `and` and `or` operators?
A: 
   - `and`: Evaluates from left to right. If the first expression is False, 
     Python skips evaluating the second expression because the result must be False.
   - `or`: If the first expression is True, Python skips evaluating the second 
     expression because the overall result must be True.

Q7: What is the Python Ternary Operator and its syntax?
A: It provides a 1-line inline conditional expression.
   Syntax: `value_if_true if condition else value_if_false`
   Example: `status = "Adult" if age >= 18 else "Minor"`

Q8: What is Truth Value Testing in Python? Which values evaluate to False?
A: In Python, any object can be tested for truth value in an `if` condition.
   The following evaluate to `False`:
   - `None`, `False`
   - Zero of any numeric type: `0`, `0.0`, `0j`
   - Empty sequences and collections: `""`, `()`, `[]`, `{}`, `set()`
   All other values evaluate to `True`.
"""

def demo_decision_making(marks):
    # Grade Evaluation using if-elif-else
    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    elif marks >= 50:
        return "Grade C"
    else:
        return "Fail"


# ==============================================================================
# SECTION 3: LOOPS & ITERATION (WHILE & FOR)
# ==============================================================================

"""
Q9: Explain the `for...else` and `while...else` construct in Python.
A: The `else` block attached to a loop executes ONLY IF the loop finishes 
   normally (i.e., without encountering a `break` statement).
   If a `break` statement exits the loop early, the `else` block is skipped.

Q10: What is the difference between `break`, `continue`, and `pass`?
A: 
   - `break`: Terminates the loop immediately and moves execution outside the loop.
   - `continue`: Skips the rest of the current iteration and jumps to the next iteration.
   - `pass`: A null statement/placeholder. Does nothing; used to fill empty syntactical blocks.

Q11: How does `range()` work, and why is it memory efficient?
A: `range(start, stop, step)` generates a sequence of numbers on demand.
   It returns a range object (an immutable sequence) which computes values 
   lazily rather than storing all numbers in memory at once.
"""

def demo_loops():
    # Search prime with for-else
    num = 17
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is Prime (for-else executed)")

    # Digit operations with while loop
    n = 12345
    rev = 0
    digit_sum = 0
    while n > 0:
        d = n % 10
        digit_sum += d
        rev = rev * 10 + d
        n //= 10
    print(f"Reversed: {rev}, Digit Sum: {digit_sum}")


# ==============================================================================
# SECTION 4: STRINGS & SLICING
# ==============================================================================

"""
Q12: Why are Python strings immutable? What happens when you modify a string?
A: Strings are immutable to ensure security, hashability (so they can be used 
   as dictionary keys), and memory optimization (string interning). 
   Modifying a string creates a NEW string object in memory rather than altering 
   the existing one.

Q13: Explain negative slicing in Python: `s[start:stop:step]`.
A: 
   - Positive index starts from 0 (left-to-right).
   - Negative index starts from -1 (right-to-left).
   - `s[::-1]` reverses a string because step is -1.
   - `s[::2]` takes every second character.

Q14: What is the difference between `find()` and `index()` methods?
A: 
   - `s.find(sub)`: Returns the lowest index where substring `sub` is found. 
     Returns `-1` if not found.
   - `s.index(sub)`: Works like `find()`, but raises a `ValueError` if `sub` is not found.
"""

def demo_strings():
    text = "Python Programming"
    
    # Slicing techniques
    print("Reversed:", text[::-1])
    print("Every second char:", text[::2])
    print("Substring:", text[7:18])
    
    # Case manipulations
    print("Title:", text.title())
    print("Swapcase:", text.swapcase())
    
    # Check Palindrome (Case Insensitive)
    s = "Madam"
    is_palindrome = s.lower() == s.lower()[::-1]
    print(f"Is '{s}' palindrome?: {is_palindrome}")


# ==============================================================================
# SECTION 5: FUNCTIONS, SCOPE, *ARGS & **KWARGS
# ==============================================================================

"""
Q15: Explain LEGB rule for variable scope resolution in Python.
A: LEGB stands for:
   1. L - Local: Names declared inside a function.
   2. E - Enclosing: Names in outer/enclosing functions (nonlocal).
   3. G - Global: Names declared at top-level of module.
   4. B - Built-in: Python's built-in module names (len, print, sum).

Q16: What is the difference between `*args` and `**kwargs`?
A: 
   - `*args`: Collects extra positional arguments into a TUPLE.
   - `**kwargs`: Collects extra keyword arguments into a DICTIONARY.
   Order in definition: `def func(positional, *args, **kwargs)`

Q17: What is recursion? What is a base case and stack overflow?
A: Recursion is when a function calls itself.
   - Base Case: A condition that stops recursion. Without it, the function calls 
     itself indefinitely until hitting `RecursionError` (Stack Overflow).

Q18: What is a Lambda function?
A: An anonymous, single-expression function created using the `lambda` keyword.
   Syntax: `lambda arguments: expression`
   Example: `square = lambda x: x ** 2`
"""

def demo_functions():
    # *args & **kwargs demonstration
    def calculate_total(*args, **kwargs):
        base_sum = sum(args)
        discount = kwargs.get("discount", 0)
        tax = kwargs.get("tax", 0)
        total = base_sum * (1 - discount / 100) * (1 + tax / 100)
        return total

    print("Total Bill:", calculate_total(100, 200, 50, discount=10, tax=5))

    # Recursive Factorial
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    print("5! =", factorial(5))


# ==============================================================================
# SECTION 6: COLLECTIONS (LISTS, DICTIONARIES, SETS, TUPLES)
# ==============================================================================

"""
Q19: Compare List, Tuple, Set, and Dictionary.
A: 
   - List: Ordered, Mutable, Allows Duplicates -> `[1, 2, 3]`
   - Tuple: Ordered, Immutable, Allows Duplicates -> `(1, 2, 3)`
   - Set: Unordered, Mutable, Unique Items Only -> `{1, 2, 3}`
   - Dict: Key-Value Pairs, Mutable, Unique Keys -> `{"a": 1}`

Q20: What is List Comprehension, Dict Comprehension, and Set Comprehension?
A: Compact syntax to create collections from iterables.
   - List Comp: `[x**2 for x in range(5) if x % 2 == 0]` -> `[0, 4, 16]`
   - Dict Comp: `{x: x**2 for x in range(4)}` -> `{0: 0, 1: 1, 2: 4, 3: 9}`
   - Set Comp: `{x for x in "banana"}` -> `{'b', 'a', 'n'}`

Q21: Why are dictionary lookups O(1) time complexity?
A: Python dictionaries use Hash Tables. When accessing `dict[key]`, Python 
   computes `hash(key)` to directly calculate the memory address of the value, 
   allowing average O(1) constant time access.

Q22: Difference between `dict.get(key)` and `dict[key]`?
A: 
   - `dict[key]` raises `KeyError` if key does not exist.
   - `dict.get(key, default)` returns `None` (or default value) if key does not exist.
"""

def demo_collections():
    # Frequency count using dict.get()
    text = "programming"
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    print("Char Frequency:", freq)

    # Merge lists without duplicates while preserving order
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    merged_unique = list(dict.fromkeys(list1 + list2))
    print("Merged Unique List:", merged_unique)

    # Flattening 2D matrix with List Comprehension
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [item for row in matrix for item in row]
    print("Flattened Matrix:", flat)


# ==============================================================================
# SECTION 7: ALGORITHMS & SPECIAL NUMBERS
# ==============================================================================

"""
Q23: What is an Armstrong Number?
A: A number that equals the sum of its own digits each raised to the power of 
   the total number of digits.
   Example: 153 -> 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

Q24: What is a Perfect Number?
A: A positive integer equal to the sum of its proper positive divisors (excluding itself).
   Example: 6 -> 1 + 2 + 3 = 6.

Q25: Compare Linear Search vs Binary Search.
A: 
   - Linear Search: Scans sequentially. Works on unsorted data. Time: O(N).
   - Binary Search: Repeatedly divides sorted range in half. Requires sorted data. Time: O(log N).
"""

def demo_algorithms():
    # Armstrong Check
    def is_armstrong(n):
        digits = str(n)
        p = len(digits)
        return sum(int(d) ** p for d in digits) == n

    print("Is 153 Armstrong?:", is_armstrong(153))

    # Second Largest Element in List (O(N) single pass)
    def find_second_largest(nums):
        first = second = float('-inf')
        for n in nums:
            if n > first:
                second = first
                first = n
            elif first > n > second:
                second = n
        return second if second != float('-inf') else None

    print("Second Largest in [10, 20, 4, 45, 99]:", find_second_largest([10, 20, 4, 45, 99]))


# ==============================================================================
# SECTION 8: ADVANCED PYTHON TECHNICAL INTERVIEW CONCEPTS
# ==============================================================================

"""
Q26: What is the difference between Shallow Copy and Deep Copy?
A: 
   - Shallow Copy (`copy.copy()`): Copies object structure, but references 
     nested objects. Changes to nested objects affect both original and copy.
   - Deep Copy (`copy.deepcopy()`): Recursively copies object AND all nested 
     objects completely independent in memory.

Q27: How does Memory Management & Garbage Collection work in Python?
A: 
   - Reference Counting: Python tracks how many references point to an object. 
     When reference count hits 0, memory is freed immediately.
   - Generational Garbage Collector: Solves cyclic references (e.g., Object A 
     references Object B, and Object B references Object A) using 3 generations (Gen 0, 1, 2).

Q28: What is `__name__ == "__main__"` used for?
A: It checks whether the Python script is being run directly from terminal/IDE 
   or imported as a module in another script.
   If run directly, `__name__` is `"__main__"`.
"""

import copy

def demo_advanced():
    # Shallow vs Deep Copy Demo
    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    original[0][0] = 999
    print("Original after mutation:", original)  # [[999, 2], [3, 4]]
    print("Shallow Copy (affected):", shallow)   # [[999, 2], [3, 4]]
    print("Deep Copy (unaffected):", deep)      # [[1, 2], [3, 4]]


# ==============================================================================
# MAIN EXECUTION ENTRY POINT
# ==============================================================================

if __name__ == "__main__":
    print("=== 1. BASICS & OPERATORS ===")
    demo_basics()
    
    print("\n=== 2. DECISION MAKING ===")
    print(demo_decision_making(85))
    
    print("\n=== 3. LOOPS ===")
    demo_loops()
    
    print("\n=== 4. STRINGS ===")
    demo_strings()
    
    print("\n=== 5. FUNCTIONS & RECURSION ===")
    demo_functions()
    
    print("\n=== 6. COLLECTIONS ===")
    demo_collections()
    
    print("\n=== 7. ALGORITHMS ===")
    demo_algorithms()
    
    print("\n=== 8. ADVANCED INTERVIEW CONCEPTS ===")
    demo_advanced()
    
    print("\n[OK] Technical Q&A document loaded and executed successfully!")
