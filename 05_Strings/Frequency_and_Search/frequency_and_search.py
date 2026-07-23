# ============================================================
#  TOPIC: Strings — Frequency & Search
# ============================================================

# DEFINITION:
#   Frequency problems count how often characters or words appear.
#   Search problems find, locate, or filter specific elements.

# ── CHARACTER FREQUENCY ───────────────────────────────────
# Count how many times each character appears in a string.

s = "banana"

# Method 1: Using a dictionary manually
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)    # {'b': 1, 'a': 3, 'n': 2}

# Method 2: dict.get() (cleaner)
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Method 3: Using collections.Counter (most Pythonic)
from collections import Counter
freq = Counter(s)
print(freq)    # Counter({'a': 3, 'n': 2, 'b': 1})

# ── LARGEST / MOST FREQUENT CHARACTER ────────────────────
s = "aababccc"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Find character with highest count:
max_char = max(freq, key=freq.get)
print("Most frequent:", max_char)       # c

# Or using Counter:
from collections import Counter
most_common = Counter(s).most_common(1)[0]
print(most_common)   # ('c', 3)

# ── UNIQUE CHARACTERS ─────────────────────────────────────
# Characters that appear exactly ONCE.

s = "abracadabra"
freq = Counter(s)
unique = [ch for ch in s if freq[ch] == 1]
print("Unique chars:", unique)    # ['c', 'd']

# Remove duplicates, keep order:
seen = set()
result = ""
for ch in s:
    if ch not in seen:
        result += ch
        seen.add(ch)
print("No duplicates:", result)   # abrcd

# ── FIRST REPEATING CHARACTER ─────────────────────────────
# First character that appears more than once.

s = "abcabd"
seen = set()
first_repeat = None
for ch in s:
    if ch in seen:
        first_repeat = ch
        break
    seen.add(ch)
print("First repeating:", first_repeat)   # a

# ── STRING SEARCH METHODS ─────────────────────────────────

s = "Hello World Python"

# find(): returns index of first match, -1 if not found
print(s.find("World"))    # 6
print(s.find("Java"))     # -1

# index(): like find() but raises ValueError if not found
print(s.index("World"))   # 6

# count(): number of times a substring appears
print(s.count("l"))       # 3

# in operator: check if substring exists
print("Python" in s)      # True
print("Java" in s)        # False

# startswith() / endswith():
print(s.startswith("Hello"))    # True
print(s.endswith("Python"))     # True

# ── SEARCH IN WORD LIST ───────────────────────────────────

sentence = "the quick brown fox jumps"
words = sentence.split()      # ['the', 'quick', 'brown', 'fox', 'jumps']

# Longest word:
longest = max(words, key=len)
print("Longest word:", longest)    # quick / jumps

# Words starting with a specific letter:
filtered = [w for w in words if w.startswith("q")]
print(filtered)    # ['quick']

# KEY POINTS:
#   → dict.get(key, 0) avoids KeyError — returns 0 if key missing
#   → Counter from collections is the most efficient for frequency
#   → find() is safe (returns -1), index() raises error if not found
#   → Use set() to track visited elements in O(1) time
