# ============================================================
#  TOPIC: Strings — Basics (Slicing & Indexing)
# ============================================================

# DEFINITION:
#   A string is a sequence of characters enclosed in quotes.
#   Each character has an index (position), starting from 0.
#   Strings are IMMUTABLE — you cannot change individual characters.

# CREATING STRINGS:
s1 = "Hello"
s2 = 'World'
s3 = """Multi
line string"""

# ── INDEXING ──────────────────────────────────────────────
# Positive index: left to right, starts at 0
# Negative index: right to left, starts at -1

s = "Python"
#     P  y  t  h  o  n
#     0  1  2  3  4  5   ← positive
#    -6 -5 -4 -3 -2 -1   ← negative

print(s[0])     # P  (first character)
print(s[-1])    # n  (last character)
print(s[2])     # t
print(s[-2])    # o

# ── SLICING ───────────────────────────────────────────────
# SYNTAX:  string[start : stop : step]
#   start → index to start from (included)
#   stop  → index to stop before (excluded)
#   step  → how many to jump (default = 1)

s = "Python"
print(s[0:3])    # Pyt   (index 0,1,2 — stop 3 is excluded)
print(s[2:5])    # tho
print(s[:3])     # Pyt   (from beginning)
print(s[3:])     # hon   (to the end)
print(s[:])      # Python (full copy)

# Reverse a string (step = -1):
print(s[::-1])   # nohtyP

# Step slicing:
print(s[::2])    # Pto   (every 2nd character)
print(s[1::2])   # yhn

# ── STRING LENGTH ──────────────────────────────────────────
print(len("hello"))     # 5
print(len(""))          # 0

# ── STRING CONCATENATION & REPETITION ────────────────────
a = "Hello"
b = "World"
print(a + " " + b)      # Hello World  (join strings)
print(a * 3)            # HelloHelloHello  (repeat)

# ── VOWELS IN A STRING ────────────────────────────────────
s = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel count:", count)    # 3

# Or using list comprehension:
vowel_list = [ch for ch in s if ch in "aeiouAEIOU"]
print(vowel_list)   # ['e', 'o', 'o']

# ── STRING CHECKING ───────────────────────────────────────
s = "Hello123"
print(s.isalpha())    # False (has digits)
print(s.isdigit())    # False (has letters)
print(s.isalnum())    # True  (only letters + digits)
print("  ".isspace()) # True

# ── in / not in ───────────────────────────────────────────
s = "Hello World"
print("World" in s)       # True
print("Python" not in s)  # True

# KEY POINTS:
#   → Strings are immutable: s[0] = "X" ← will cause an ERROR
#   → s[::-1] is the cleanest way to reverse a string
#   → Slicing never raises IndexError — it simply adjusts
#   → len() is 0-based count, indexing is 0-based access
