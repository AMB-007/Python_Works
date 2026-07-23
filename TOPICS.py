# ============================================================
#              PYTHON_WORKS - TOPICS OVERVIEW
# ============================================================
# A brief reference of every topic covered in this workspace.
# Each section maps to a folder and its key concepts.
# ============================================================


# ─────────────────────────────────────────────────────────────
# 01_Basics
# ─────────────────────────────────────────────────────────────

# Calculations/
#   average_of_5_subject  → Average of 5 subject marks
#   bill_cost             → Calculate total bill with tax
#   bmi                   → Body Mass Index = weight / height²
#   bmr                   → Basal Metabolic Rate formula
#   electricity           → Monthly electricity bill cost
#   input_calculator      → Basic +, -, *, / using input()
#   rectangle_area_perimeter → Area = l*b, Perimeter = 2*(l+b)
#   simple_intrest        → SI = (P * R * T) / 100

# Conversions/
#   celcius_fahrenheit    → F = (C * 9/5) + 32
#   convert_years_into_days   → years → days (×365)
#   day_hour_minute_seconds_conversion → total seconds → D/H/M/S

# IO_and_Variables/
#   basic_arithmetic      → input() + int() + arithmetic ops
#   shift_zeros_to_end    → move all 0s to end of a list
#   split_bill            → divide total among n people

# Operators/
#   assignment_operators  → =, +=, -=, *=, /=, //=, **=, %=
#   comparison            → ==, !=, >, <, >=, <=
#   square_cube_squareroot → **, math.sqrt()
#   swap_two_no           → swap with temp / without temp / XOR


# ─────────────────────────────────────────────────────────────
# 02_Decision_Making
# ─────────────────────────────────────────────────────────────

# If_Else/              → if / elif / else branching
# Logical_Operators/    → and, or, not in conditions
# Nested_If/            → if inside another if
# Ternary_Operator/     → value_if_true if condition else value_if_false


# ─────────────────────────────────────────────────────────────
# 03_While_Loops
# ─────────────────────────────────────────────────────────────

# Basics/           → while condition: ... , break, continue
# Number_Problems/  → digit sum, reverse digits, count digits
# Special_Numbers/  → Armstrong, palindrome, prime via while loop


# ─────────────────────────────────────────────────────────────
# 04_For_Loops
# ─────────────────────────────────────────────────────────────

# Basics/           → for i in range(), iterating lists/strings
# Number_Problems/  → sum of n, multiplication table, FizzBuzz
# Range_Programs/   → range(start, stop, step) patterns
# Special_Numbers/  → perfect number, prime, Armstrong via for loop


# ─────────────────────────────────────────────────────────────
# 05_Strings
# ─────────────────────────────────────────────────────────────

# Basics/
#   string_slicing    → s[start:stop:step], s[::-1] (reverse)
#   vowels            → count/find vowels in a string

# Case_and_Characters/
#   char_frequency_string  → count occurrences of each character
#   count_character        → count a specific char in string
#   lower_and_uppercase    → .lower(), .upper(), .swapcase(), .title()
#   palindrome             → check if string reads same backwards
#   second_char            → find/print second character

# Frequency_and_Search/
#   first_repeating        → first character that repeats
#   frequency              → frequency of each char using dict
#   largest_frequency      → char with highest frequency
#   unique                 → remove/find non-repeating characters

# Key String Methods:
#   s.upper()      → "hello" → "HELLO"
#   s.lower()      → "HELLO" → "hello"
#   s.title()      → "hello world" → "Hello World"
#   s.strip()      → removes leading/trailing whitespace
#   s.split(",")   → splits into list by delimiter
#   s.replace(a,b) → replace all occurrences of a with b
#   s.find(x)      → index of first occurrence (-1 if not found)
#   s.count(x)     → count occurrences of x
#   s.startswith() → True/False
#   s.endswith()   → True/False
#   s[::-1]        → reverse a string
#   s.isdigit()    → True if all chars are digits
#   s.isalpha()    → True if all chars are alphabets
#   len(s)         → length of string


# ─────────────────────────────────────────────────────────────
# 06_Patterns
# ─────────────────────────────────────────────────────────────

# star_patterns   → *, right triangle, pyramid, diamond using loops
# exam_pattern    → custom pattern for practice


# ─────────────────────────────────────────────────────────────
# 07_Functions
# ─────────────────────────────────────────────────────────────

# Basics/
#   function_intro          → def func():, return, calling functions
#   add_num                 → function with parameters
#   count_vowels            → count vowels using a function
#   count_uppercase         → count uppercase letters via function
#   default_and_positional_args → def f(a, b=10): positional & default
#   integer_n_is_within_100or200 → range check inside a function
#   reverse_numbers         → reverse a number using function
#   sum_digits              → sum of digits using a function

# Args_and_Kwargs/
#   args_kwargs → *args (variable positional), **kwargs (variable keyword)
#                 def f(*args, **kwargs): ...

# Math_Functions/
#   armstrong  → sum(digit**n for digit in num) == num
#   is.prime   → divisible only by 1 and itself
#   perfect    → sum of divisors == number (e.g. 6 = 1+2+3)

# Recursion/
#   factorial           → n! = n * (n-1)!  base: 0! = 1
#   factorial_dup1      → alternate factorial approach
#   recursive_factorial → clean recursive implementation

# String_Functions/
#   anagram        → two strings with same chars (sorted comparison)
#   panagram       → sentence containing every letter a-z
#   remove_duplicate_chars_func → keep only first occurrence of each char
#   reverse_before_p → reverse characters before letter 'p'


# ─────────────────────────────────────────────────────────────
# 08_Collections
# ─────────────────────────────────────────────────────────────

# Dictionaries/
#   nested_dict_operations → dict inside dict, access & update nested keys
#   Key Methods:
#     d.keys()    → all keys
#     d.values()  → all values
#     d.items()   → (key, value) pairs
#     d.get(k)    → get value safely (no KeyError)
#     d.update()  → merge another dict
#     d.pop(k)    → remove key and return value

# List_Comprehension/
#   list_comprehension_intro → [expr for item in iterable if condition]
#   Examples:
#     squares  = [x**2 for x in range(10)]
#     evens    = [x for x in range(20) if x % 2 == 0]
#     filtered = [x for x in lst if x > 5]

# List_Operations/
#   create_list_1_to_n    → list(range(1, n+1))
#   even_remove           → remove even numbers from list
#   frequency             → count frequency of each element
#   largest_with_max_freq → element with highest frequency
#   list_sum_max_min      → sum(), max(), min() built-ins
#   merge_lists_no_duplicates → list(set(a + b))
#   non_prime             → filter non-prime numbers from list
#   Key Methods:
#     lst.append(x)   → add to end
#     lst.insert(i,x) → insert at index
#     lst.remove(x)   → remove first occurrence
#     lst.pop()       → remove and return last item
#     lst.sort()      → sort in place
#     sorted(lst)     → return new sorted list
#     lst.reverse()   → reverse in place
#     lst.index(x)    → index of element
#     lst.count(x)    → count occurrences

# Searching_and_Sorting/
#   largest        → find largest without max()
#   largest_word   → longest word in a sentence
#   missing_number → find missing from 1..n using sum formula
#   second_largest → second largest without sort
#   smallest       → find smallest without min()


# ─────────────────────────────────────────────────────────────
# 09_Tasks
# ─────────────────────────────────────────────────────────────
# Practice problem sets organized by date.
# Each date folder contains mixed problems covering all topics.


# ─────────────────────────────────────────────────────────────
# Python-practice/
# ─────────────────────────────────────────────────────────────
# Miscellaneous practice programs and experiments.
