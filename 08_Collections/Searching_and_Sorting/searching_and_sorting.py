# ============================================================
#  TOPIC: Collections — Searching & Sorting
# ============================================================

# DEFINITION:
#   Searching means finding a specific element or value in a list.
#   Sorting means arranging elements in a specific order.
#   These are fundamental data manipulation skills.

# ── FINDING LARGEST / SMALLEST ────────────────────────────

lst = [5, 3, 8, 1, 9, 2]

# Using built-ins (simplest):
print(max(lst))    # 9
print(min(lst))    # 1

# Without max()/min() — manual approach:
largest = lst[0]
for x in lst:
    if x > largest:
        largest = x
print("Largest:", largest)    # 9

smallest = lst[0]
for x in lst:
    if x < smallest:
        smallest = x
print("Smallest:", smallest)  # 1

# ── SECOND LARGEST ────────────────────────────────────────
# Remove the max, then find max of the rest.

lst = [5, 3, 8, 1, 9, 2]

# Method 1: sort and pick second-to-last unique
unique = list(set(lst))
unique.sort()
print("Second largest:", unique[-2])    # 8

# Method 2: manual (without sort)
first = second = float('-inf')
for x in lst:
    if x > first:
        second = first
        first = x
    elif x > second and x != first:
        second = x
print("Second largest:", second)        # 8

# ── MISSING NUMBER ────────────────────────────────────────
# Find the one missing number from a list of 1 to n.
# Formula: sum(1..n) = n*(n+1)/2

lst = [1, 2, 4, 5, 6]   # missing 3
n = 6
expected = n * (n + 1) // 2
actual = sum(lst)
print("Missing:", expected - actual)    # 3

# ── LARGEST WORD IN A SENTENCE ────────────────────────────
sentence = "I love Python programming"
words = sentence.split()

longest = max(words, key=len)
print("Longest word:", longest)    # programming

# Manual approach:
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word

# ── SORTING ───────────────────────────────────────────────

lst = [5, 2, 8, 1, 9]

# sorted() → returns NEW sorted list (original unchanged)
new_lst = sorted(lst)
print(new_lst)    # [1, 2, 5, 8, 9]
print(lst)        # [5, 2, 8, 1, 9]  ← unchanged

# .sort() → sorts IN PLACE (modifies original)
lst.sort()
print(lst)        # [1, 2, 5, 8, 9]

# Descending:
lst.sort(reverse=True)
print(lst)        # [9, 8, 5, 2, 1]

# Sort strings by length:
words = ["banana", "apple", "fig", "cherry"]
words.sort(key=len)
print(words)    # ['fig', 'apple', 'banana', 'cherry']

# Sort by last character:
words.sort(key=lambda w: w[-1])

# ── LINEAR SEARCH ─────────────────────────────────────────
# Check each element one by one.

def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i    # found at index i
    return -1           # not found

lst = [4, 2, 7, 1, 9]
print(linear_search(lst, 7))    # 2
print(linear_search(lst, 5))    # -1

# ── BINARY SEARCH (on sorted list) ────────────────────────
# Efficient: halves the search space each time. O(log n).

def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = [1, 3, 5, 7, 9, 11]
print(binary_search(lst, 7))    # 3
print(binary_search(lst, 4))    # -1

# KEY POINTS:
#   → sorted() keeps original safe; .sort() modifies in place
#   → max(lst, key=fn) lets you define WHAT to compare
#   → Missing number trick: use the sum formula n*(n+1)//2
#   → Binary search REQUIRES a sorted list first
#   → Linear search: O(n) time; Binary search: O(log n) time
