# ============================================================
#  TOPIC: Functions — String Functions
# ============================================================

# DEFINITION:
#   String functions solve text-based problems using Python's
#   built-in string methods and custom logic inside functions.

# ── ANAGRAM ───────────────────────────────────────────────
# DEFINITION: Two strings are anagrams if they contain the
#             SAME characters in ANY order.
# Example: "listen" and "silent" → both have l,i,s,t,e,n

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False
print(is_anagram("Triangle", "Integral"))  # True

# Alternative using Counter:
from collections import Counter
def is_anagram_v2(s1, s2):
    return Counter(s1.lower()) == Counter(s2.lower())

# ── PANGRAM ───────────────────────────────────────────────
# DEFINITION: A sentence that contains EVERY letter of the
#             alphabet at least once.
# Example: "The quick brown fox jumps over the lazy dog"

def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet <= set(sentence.lower())
    # <= means: is alphabet a subset of the sentence characters?

print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("Hello World"))                                  # False

# ── REMOVE DUPLICATE CHARACTERS ───────────────────────────
# Keep only the FIRST occurrence of each character, in order.

def remove_duplicates(s):
    seen = set()
    result = ""
    for ch in s:
        if ch not in seen:
            result += ch
            seen.add(ch)
    return result

print(remove_duplicates("banana"))      # ban
print(remove_duplicates("programming")) # progamin

# ── REVERSE STRING BEFORE 'p' ─────────────────────────────
# Reverse the portion of the string that comes before 'p'.

def reverse_before_p(s):
    idx = s.find("p")
    if idx == -1:
        return s[::-1]       # no 'p' found, reverse whole string
    return s[:idx][::-1] + s[idx:]

print(reverse_before_p("abcpdef"))   # cbapdef
print(reverse_before_p("hello"))     # olleh

# ── MORE COMMON STRING FUNCTION PROBLEMS ──────────────────

# Count words in a sentence:
def count_words(s):
    return len(s.split())

print(count_words("Hello World Python"))    # 3

# Reverse words in a sentence:
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("Hello World"))    # World Hello

# Check if all characters are unique:
def all_unique(s):
    return len(s) == len(set(s))

print(all_unique("abcde"))   # True
print(all_unique("aabcd"))   # False

# Title case each word:
def to_title(s):
    return " ".join(word.capitalize() for word in s.split())

print(to_title("the quick brown fox"))  # The Quick Brown Fox

# KEY POINTS:
#   → Anagram: sorted() is the simplest approach
#   → Pangram: use set() to check if all 26 letters are present
#   → Remove duplicates: use a set to track already-seen characters
#   → s.split() splits by whitespace by default → returns list of words
#   → " ".join(list) → combines list of words back into a string
