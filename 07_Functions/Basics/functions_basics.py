# ============================================================
#  TOPIC: Functions — Basics
# ============================================================

# DEFINITION:
#   A function is a reusable block of code that performs a
#   specific task. Define it once, call it multiple times.
#   Functions help avoid repetition and make code organized.

# ── DEFINING A FUNCTION ───────────────────────────────────
# SYNTAX:
#   def function_name(parameters):
#       """docstring (optional description)"""
#       # body
#       return value   ← optional

# Simple function with no parameters:
def greet():
    print("Hello!")

greet()     # calling the function → Hello!

# ── PARAMETERS & ARGUMENTS ───────────────────────────────
# Parameters: variables listed in the function definition
# Arguments:  actual values passed when calling the function

def add(a, b):          # a, b are parameters
    return a + b

result = add(5, 3)      # 5, 3 are arguments
print(result)           # 8

# ── RETURN STATEMENT ──────────────────────────────────────
# return sends a value back to the caller.
# A function without return gives None.

def square(n):
    return n * n

print(square(5))        # 25

# Return multiple values:
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 9, 2])
print(lo, hi)           # 1 9

# ── DEFAULT ARGUMENTS ──────────────────────────────────────
# A default value is used if no argument is provided.

def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Arjun")              # Hello, Arjun!   (uses default)
greet("Arjun", "Welcome")   # Welcome, Arjun! (overrides default)

# ── POSITIONAL vs KEYWORD ARGUMENTS ─────────────────────
def student(name, age, grade):
    print(f"{name}, Age: {age}, Grade: {grade}")

student("Arjun", 21, "A")                       # positional
student(grade="A", name="Arjun", age=21)        # keyword (any order)
student("Arjun", grade="A", age=21)             # mixed

# ── COMMON FUNCTION EXAMPLES ──────────────────────────────

# Count vowels in a string:
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

print(count_vowels("Hello"))    # 2

# Count uppercase letters:
def count_upper(s):
    return sum(1 for ch in s if ch.isupper())

print(count_upper("Hello World"))   # 2

# Check if integer n is between 100 and 200:
def in_range(n):
    return 100 <= n <= 200

print(in_range(150))    # True
print(in_range(50))     # False

# Reverse a number using function:
def reverse_num(n):
    return int(str(n)[::-1])

print(reverse_num(1234))    # 4321

# Sum of digits:
def digit_sum(n):
    return sum(int(d) for d in str(n))

print(digit_sum(1234))    # 10

# KEY POINTS:
#   → def keyword defines a function
#   → Parameters with defaults must come AFTER non-default ones
#   → A function can return multiple values as a tuple
#   → Call a function by writing its name followed by ()
#   → Functions can call other functions (composition)
