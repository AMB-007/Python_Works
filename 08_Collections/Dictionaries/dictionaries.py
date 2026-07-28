# Question: Write a Python program for dictionaries.

# ============================================================
#  TOPIC: Collections â€” Dictionaries
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

# â”€â”€ ACCESSING VALUES â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
print(student["name"])           # Arjun  (KeyError if not found)
print(student.get("age"))        # 21
print(student.get("score", 0))   # 0  (default if key missing â€” NO error)

# â”€â”€ ADDING / UPDATING â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
student["city"] = "Chennai"      # add new key
student["age"] = 22              # update existing key
student.update({"grade": "A+", "score": 95})  # update multiple

# â”€â”€ REMOVING â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
student.pop("city")              # remove key, return its value
del student["score"]             # delete key (no return)
student.clear()                  # empty the entire dict

# â”€â”€ ITERATING OVER A DICTIONARY â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
d = {"a": 1, "b": 2, "c": 3}

for key in d:                    # iterate keys
    print(key)

for key in d.keys():             # same â€” all keys
    print(key)

for value in d.values():         # all values
    print(value)

for key, value in d.items():     # key-value pairs (most used)
    print(f"{key} â†’ {value}")

# â”€â”€ KEY METHODS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
d = {"x": 10, "y": 20, "z": 30}

print(d.keys())     # dict_keys(['x', 'y', 'z'])
print(d.values())   # dict_values([10, 20, 30])
print(d.items())    # dict_items([('x', 10), ('y', 20), ('z', 30)])
print("x" in d)    # True  (key check)
print(len(d))       # 3

# â”€â”€ NESTED DICTIONARY â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
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

# â”€â”€ BUILDING FREQUENCY DICT â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)    # {'apple': 3, 'banana': 2, 'cherry': 1}

# Most common:
most_freq = max(freq, key=freq.get)
print(most_freq)   # apple

# â”€â”€ DICT COMPREHENSION â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(1, 6)}
print(squares)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# KEY POINTS:
#   â†’ Use .get(key, default) to avoid KeyError
#   â†’ Keys must be immutable; values can be anything
#   â†’ dict.items() is the most common way to loop dicts
#   â†’ Dictionaries maintain insertion order in Python 3.7+
#   â†’ Checking "key in dict" is O(1) â€” very fast

