# ============================================================
#  TOPIC: Strings — Case & Character Operations
# ============================================================

# DEFINITION:
#   Python provides built-in string methods to change the case
#   of characters, check character types, and work with
#   individual characters in a string.

# ── CASE METHODS ──────────────────────────────────────────

s = "hello WORLD"

print(s.upper())       # HELLO WORLD   → all uppercase
print(s.lower())       # hello world   → all lowercase
print(s.title())       # Hello World   → first letter of each word uppercase
print(s.capitalize())  # Hello world   → only very first letter uppercase
print(s.swapcase())    # HELLO world   → flips upper↔lower for each char

# ── CHARACTER METHODS ─────────────────────────────────────

s = "Hello123!"

print(s.isalpha())   # False → True only if ALL chars are letters
print(s.isdigit())   # False → True only if ALL chars are digits
print(s.isalnum())   # False → True only if letters AND/OR digits (no symbols)
print(s.isupper())   # False → True if ALL letters are uppercase
print(s.islower())   # False → True if ALL letters are lowercase
print(s.isspace())   # False → True if string contains only whitespace

# Examples:
print("HELLO".isupper())    # True
print("hello".islower())    # True
print("Hello123".isalnum()) # True

# ── COUNTING SPECIFIC CHARACTERS ──────────────────────────

s = "Hello World"

# Count uppercase letters:
count = sum(1 for ch in s if ch.isupper())
print("Uppercase:", count)    # 2 (H, W)

# Count lowercase letters:
count = sum(1 for ch in s if ch.islower())
print("Lowercase:", count)    # 8

# Count digits:
s2 = "abc123def456"
count = sum(1 for ch in s2 if ch.isdigit())
print("Digits:", count)       # 6

# ── PALINDROME CHECK ──────────────────────────────────────
# DEFINITION: A string that reads the same forwards and backwards.

s = "racecar"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Case-insensitive palindrome:
s = "Madam"
if s.lower() == s.lower()[::-1]:
    print("Palindrome")      # Palindrome

# ── CHARACTER FREQUENCY ───────────────────────────────────
# How many times each character appears

s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)    # {'b': 1, 'a': 3, 'n': 2}

# Or with s.count():
print(s.count("a"))   # 3

# ── SECOND CHARACTER / NTH CHARACTER ─────────────────────
s = "Python"
print(s[1])         # y  (second character, 0-indexed)
print(s[-1])        # n  (last character)

# Every second character:
print(s[::2])       # Pto

# ── ord() and chr() ───────────────────────────────────────
# ord(char) → ASCII value of a character
# chr(num)  → character from ASCII value

print(ord('A'))     # 65
print(ord('a'))     # 97
print(chr(65))      # A
print(chr(97))      # a

# Check if character is uppercase using ASCII:
ch = 'G'
if 65 <= ord(ch) <= 90:
    print("Uppercase")

# KEY POINTS:
#   → Methods don't change the original string — they return a NEW string
#   → s.count(x) counts how many times x appears in s
#   → Palindrome trick: compare s with s[::-1]
#   → ord() and chr() are useful for ASCII-based character problems
