# ============================================================
#  TOPIC: Collections — Dictionaries
# ============================================================

# DEFINITION:
#   A dictionary is an UNORDERED collection of KEY: VALUE pairs.
#   Keys must be unique and immutable (string, int, tuple).
#   Values can be anything. Defined with curly braces: { }
#   Efficient O(1) lookup by key.

# CREATING A DICTIONARY:
student = {"name": "Arjun", "age": 21, "grade": "A"}
empty = {}
empty2 = dict()

# ── ACCESSING VALUES ──────────────────────────────────────
print(student["name"])           # Arjun  (KeyError if not found)
print(student.get("age"))        # 21
print(student.get("score", 0))   # 0  (default if key missing — NO error)

# ── ADDING / UPDATING ─────────────────────────────────────
student["city"] = "Chennai"      # add new key
student["age"] = 22              # update existing key
student.update({"grade": "A+", "score": 95})  # update multiple

# ── REMOVING ──────────────────────────────────────────────
student.pop("city")              # remove key, return its value
del student["score"]             # delete key (no return)
student.clear()                  # empty the entire dict

# ── ITERATING OVER A DICTIONARY ───────────────────────────
d = {"a": 1, "b": 2, "c": 3}

for key in d:                    # iterate keys
    print(key)

for key in d.keys():             # same — all keys
    print(key)

for value in d.values():         # all values
    print(value)

for key, value in d.items():     # key-value pairs (most used)
    print(f"{key} → {value}")

# ── KEY METHODS ───────────────────────────────────────────
d = {"x": 10, "y": 20, "z": 30}

print(d.keys())     # dict_keys(['x', 'y', 'z'])
print(d.values())   # dict_values([10, 20, 30])
print(d.items())    # dict_items([('x', 10), ('y', 20), ('z', 30)])
print("x" in d)    # True  (key check)
print(len(d))       # 3

# ── NESTED DICTIONARY ─────────────────────────────────────
# DEFINITION: A dictionary where values are themselves dictionaries.

students = {
    "Arjun": {"age": 21, "grade": "A"},
    "Ravi":  {"age": 20, "grade": "B"},
}

# Access nested:
print(students["Arjun"]["grade"])    # A

# Add new nested entry:
students["Priya"] = {"age": 22, "grade": "A+"}

# Update nested value:
students["Ravi"]["grade"] = "A"

# Loop through nested dict:
for name, info in students.items():
    print(f"{name}: Age={info['age']}, Grade={info['grade']}")

# ── BUILDING FREQUENCY DICT ───────────────────────────────
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)    # {'apple': 3, 'banana': 2, 'cherry': 1}

# Most common:
most_freq = max(freq, key=freq.get)
print(most_freq)   # apple

# ── DICT COMPREHENSION ────────────────────────────────────
# {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(1, 6)}
print(squares)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# KEY POINTS:
#   → Use .get(key, default) to avoid KeyError
#   → Keys must be immutable; values can be anything
#   → dict.items() is the most common way to loop dicts
#   → Dictionaries maintain insertion order in Python 3.7+
#   → Checking "key in dict" is O(1) — very fast
