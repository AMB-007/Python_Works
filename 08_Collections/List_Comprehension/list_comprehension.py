# ============================================================
#  TOPIC: Collections — List Comprehension
# ============================================================

# DEFINITION:
#   List comprehension is a concise, readable way to create a
#   new list by applying an expression to each item in an iterable,
#   optionally filtering with a condition.
#   It replaces multi-line for loops with a single line.

# SYNTAX:
#   [expression  for  item  in  iterable]
#   [expression  for  item  in  iterable  if  condition]

# ── BASIC EXAMPLES ────────────────────────────────────────

# Without list comprehension:
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)    # [1, 4, 9, 16, 25]

# WITH list comprehension (same result, one line):
squares = [x ** 2 for x in range(1, 6)]
print(squares)    # [1, 4, 9, 16, 25]

# ── WITH CONDITION (filtering) ────────────────────────────
# [expression for item in iterable if condition]

# Even numbers from 1 to 20:
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Odd numbers:
odds = [x for x in range(1, 21) if x % 2 != 0]

# Multiples of 3:
mult3 = [x for x in range(1, 31) if x % 3 == 0]
print(mult3)    # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# ── WITH STRINGS ──────────────────────────────────────────

# Uppercase each word:
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper)    # ['HELLO', 'WORLD', 'PYTHON']

# Get only words longer than 4 chars:
long_words = [w for w in words if len(w) > 4]
print(long_words)    # ['hello', 'world', 'python']

# Extract vowels from a string:
s = "hello world"
vowels = [ch for ch in s if ch in "aeiou"]
print(vowels)    # ['e', 'o', 'o']

# ── IF-ELSE IN COMPREHENSION ──────────────────────────────
# When using if-else, the condition goes BEFORE the for:

nums = [1, 2, 3, 4, 5, 6]
labels = ["Even" if x % 2 == 0 else "Odd" for x in nums]
print(labels)    # ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

# ── NESTED LIST COMPREHENSION ─────────────────────────────
# Creating a multiplication table (2D list):
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Flatten a 2D list:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [item for row in matrix for item in row]
print(flat)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ── PRACTICAL EXAMPLES ────────────────────────────────────

# Squares of even numbers only:
result = [x**2 for x in range(1, 11) if x % 2 == 0]
print(result)    # [4, 16, 36, 64, 100]

# Remove negative numbers from list:
lst = [-3, 1, -2, 5, -1, 8]
positives = [x for x in lst if x >= 0]
print(positives)    # [1, 5, 8]

# Get lengths of each word:
words = ["cat", "elephant", "dog", "ant"]
lengths = [len(w) for w in words]
print(lengths)    # [3, 8, 3, 3]

# KEY POINTS:
#   → Faster and more readable than a regular for loop + append
#   → if FILTER: [expr for x in lst if condition]
#   → if-ELSE: [expr1 if cond else expr2 for x in lst]  ← note position!
#   → Avoid deeply nested comprehensions — they hurt readability
#   → You can also create: set comprehension {x for x in lst}
#                          dict comprehension {k: v for k, v in items}
