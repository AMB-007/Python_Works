# ============================================================
#  TOPIC: Collections — List Operations
# ============================================================

# DEFINITION:
#   A list is an ordered, mutable (changeable) collection of items.
#   Items can be of any type. Lists allow duplicates and maintain order.
#   Defined using square brackets: [ ]

# CREATING A LIST:
nums = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# ── INDEXING & SLICING ────────────────────────────────────
lst = [10, 20, 30, 40, 50]
print(lst[0])      # 10   (first)
print(lst[-1])     # 50   (last)
print(lst[1:4])    # [20, 30, 40]
print(lst[::-1])   # [50, 40, 30, 20, 10]  (reversed)

# ── BUILT-IN LIST METHODS ─────────────────────────────────
lst = [3, 1, 4, 1, 5]

lst.append(9)       # [3,1,4,1,5,9]     → add to END
lst.insert(2, 99)   # [3,1,99,4,1,5,9]  → insert at index 2
lst.remove(1)       # removes FIRST occurrence of 1
lst.pop()           # removes and returns LAST item
lst.pop(0)          # removes and returns item at index 0
lst.sort()          # sorts in place (ascending)
lst.sort(reverse=True)  # sorts descending
lst.reverse()       # reverses in place
lst.clear()         # empties the list → []
lst_copy = lst.copy()   # shallow copy

lst = [3, 1, 4, 1, 5]
print(lst.count(1))     # 2   → count occurrences of 1
print(lst.index(4))     # 2   → index of first occurrence of 4
print(len(lst))         # 5   → number of items
print(sum(lst))         # 14  → sum of all items
print(max(lst))         # 5   → maximum value
print(min(lst))         # 1   → minimum value

# ── COMMON OPERATIONS ─────────────────────────────────────

# Create list of 1 to n:
n = 5
lst = list(range(1, n + 1))    # [1, 2, 3, 4, 5]

# Remove even numbers:
lst = [1, 2, 3, 4, 5, 6]
odd_only = [x for x in lst if x % 2 != 0]
print(odd_only)    # [1, 3, 5]

# Frequency of each element:
lst = [1, 2, 2, 3, 3, 3]
freq = {}
for item in lst:
    freq[item] = freq.get(item, 0) + 1
print(freq)    # {1: 1, 2: 2, 3: 3}

# Element with max frequency:
most_common = max(freq, key=freq.get)
print(most_common)    # 3

# Merge two lists without duplicates:
a = [1, 2, 3]
b = [3, 4, 5]
merged = list(set(a + b))
print(merged)    # [1, 2, 3, 4, 5]

# Check if list contains non-prime numbers:
def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

lst = [2, 3, 4, 5, 6]
non_primes = [x for x in lst if not is_prime(x)]
print(non_primes)    # [4, 6]

# Sum, Max, Min without built-ins:
lst = [5, 3, 8, 1, 9]
total = 0
for x in lst: total += x         # manual sum

largest = lst[0]
for x in lst:
    if x > largest: largest = x  # manual max

# ── sorted() vs .sort() ───────────────────────────────────
lst = [3, 1, 4, 1, 5]
new = sorted(lst)       # returns NEW sorted list, original unchanged
lst.sort()              # modifies ORIGINAL list in place

# KEY POINTS:
#   → Lists are mutable — you CAN change elements after creation
#   → list[index] = new_value  → directly reassign
#   → Use sorted() when you need to keep the original unchanged
#   → set(list) removes duplicates but loses order
