# 📘 Comprehensive Python Technical Theory & Method Reference Guide

> **Welcome!** This guide maps directly to the 12 folders in this repository (`01_Basics` ➔ `12_OOPs`). Each section breaks down technical theory, concepts, methods, real-world analogies, and interview Q&As corresponding to your workspace files and folders.

---

## 🧭 Repository Folder Mapping Overview

| Section | Workspace Folder | Topics Covered |
| :--- | :--- | :--- |
| **Section 1** | [01_Basics](file:///d:/Python_Works/01_Basics) | Execution flow, Variables, Memory allocation, Mutability, Calculations, Operators, Conversions |
| **Section 2** | [02_Decision_Making](file:///d:/Python_Works/02_Decision_Making) | Conditional branching, Boolean truthiness, Short-Circuit evaluation, Ternary operator |
| **Section 3** | [03_While_Loops](file:///d:/Python_Works/03_While_Loops) & [04_For_Loops](file:///d:/Python_Works/04_For_Loops) | Iteration, `range()`, `break`/`continue`/`pass`, `loop...else`, digit extraction, series |
| **Section 4** | [05_Strings](file:///d:/Python_Works/05_Strings) | String immutability & interning, Slicing `[start:stop:step]`, Case conversion, Search, Frequency |
| **Section 5** | [06_Patterns](file:///d:/Python_Works/06_Patterns) | Nested loop logic, Grid pattern generation, Star & Number pattern visualization |
| **Section 6** | [07_Functions](file:///d:/Python_Works/07_Functions) | LEGB Scope, `*args`/`**kwargs`, Lambda, Higher-Order (`map`/`filter`), Recursion, Modules & Packages |
| **Section 7** | [08_Collections](file:///d:/Python_Works/08_Collections) | Lists, Tuples, Sets, Dictionaries, Hash Table $O(1)$ lookups, List Comprehension, Searching & Sorting |
| **Section 8** | [09_Tasks](file:///d:/Python_Works/09_Tasks) | Daily challenge problem breakdown, Special numbers (Armstrong, Perfect, Palindrome, Strong) |
| **Section 9** | [10_Exception_Handling](file:///d:/Python_Works/10_Exception_Handling) | Robust code, `try`, `except`, `else`, `finally`, built-in exception hierarchy, custom exceptions |
| **Section 10** | [11_File_Handling](file:///d:/Python_Works/11_File_Handling) | Disk I/O, file modes (`r`, `w`, `a`), context managers `with open()`, file read exceptions |
| **Section 11** | [12_OOPs](file:///d:/Python_Works/12_OOPs) | Classes, Objects, `__init__`, `self`, Inheritance, Encapsulation, Polymorphism, Abstraction |
| **Section 12** | Advanced Python | Shallow/Deep Copy, Memory Management, Reference Counting, GIL, Duck Typing, `__name__ == "__main__"` |

---

## 📁 Section 1: 01_Basics — Execution, Memory & Operators

### Q1. What is Python and how does it execute code?
**Answer:**
Python is a high-level, dynamically-typed, interpreted language. Execution follows a 2-step process:

```
[ Your Code (.py) ] ──> ( Python Compiler ) ──> [ Bytecode (.pyc) ] ──> ( Python Virtual Machine PVM ) ──> [ Output ]
```

1. **Compilation:** Code is compiled into intermediate **Bytecode** (`.pyc`).
2. **Interpretation:** The **Python Virtual Machine (PVM)** executes bytecode line-by-line.

> 🔍 **Analogy:** Think of `.py` code as a recipe in English. Bytecode is the standardized musical score, and PVM is the musician playing it.

---

### Q2. How do Variables & Memory Allocation work in Python?
**Answer:**
In Python, **everything is an object**. Variables are **name tags (references)** pointing to objects in memory!

```python
x = 10
y = 10
# Both x and y point to the EXACT SAME integer object in memory!
print(id(x) == id(y))  # Output: True
```

---

### Q3. Explain Mutable vs. Immutable Data Types.
**Answer:**

> 🔍 **Analogy:**  
> - **Immutable = Sealed Glass Bottle:** Cannot change contents inside. Replacing value creates a new bottle (`id()` changes).  
> - **Mutable = Open Cardboard Box:** Can modify, add, or remove contents in-place (`id()` stays the same).

```python
# Immutable (str)
s = "Hello"
print(id(s))
s = s + " World"  # Creates NEW object!
print(id(s))      # Different ID!

# Mutable (list)
lst = [1, 2]
print(id(lst))
lst.append(3)     # Modifies IN-PLACE!
print(id(lst))    # Same ID!
```

---

### Q4. Division (`/`) vs. Floor Division (`//`) vs. Modulus (`%`)
**Answer:**

```python
print(7 / 2)   # 3.5  (Float Division — Always float)
print(7 // 2)  # 3    (Floor Division — Rounds down to whole integer)
print(-7 // 2) # -4   (Rounds down towards negative infinity!)
print(7 % 2)   # 1    (Modulus — Remainder of division)
```

---

## 📁 Section 2: 02_Decision_Making — Conditional Logic & Boolean Algebra

### Q5. Truth Value Testing: What is "Truthy" and "Falsy"?
**Answer:**
In boolean conditions (`if`/`while`), the following evaluate to `False` (**Falsy**):
- ❌ `None` and `False`
- ❌ Numeric zeros: `0`, `0.0`, `0j`
- ❌ Empty collections: `""`, `[]`, `()`, `{}`, `set()`, `range(0)`

Everything else evaluates to `True` (**Truthy**)!

---

### Q6. What is Short-Circuit Evaluation?
**Answer:**
Python evaluates `and` / `or` conditions from left to right and stops as soon as the result is determined:
- **`and`**: If the 1st condition is `False`, the rest is skipped.
- **`or`**: If the 1st condition is `True`, the rest is skipped.

---

### Q7. What is the Ternary Operator?
**Answer:**
A single-line conditional expression.
**Syntax:** `value_if_true if condition else value_if_false`
```python
age = 20
status = "Adult" if age >= 18 else "Minor"  # Output: "Adult"
```

---

## 📁 Section 3: 03_While_Loops & 04_For_Loops — Control Statements & Ranges

### Q8. Difference between `break`, `continue`, and `pass`

| Statement | Action |
| :--- | :--- |
| **`break`** | 🛑 Exits and terminates the loop immediately. |
| **`continue`** | ⏭️ Skips remainder of current iteration & jumps to next iteration. |
| **`pass`** | 🧱 Null placeholder that does nothing (satisfies syntax requirement). |

---

### Q9. How does `loop...else` work?
**Answer:**
The `else` block on a loop runs **ONLY if the loop finishes all iterations without hitting a `break`**.

```python
for num in [2, 4, 6]:
    if num == 5:
        print("Found!")
        break
else:
    print("5 not found in list!")  # Output: 5 not found in list!
```

---

### Q10. How does `range()` work in Python?
**Answer:**
`range(start, stop, step)` generates an immutable sequence of integers lazily (on demand in $O(1)$ memory).
- `start` (default 0, inclusive)
- `stop` (required, exclusive)
- `step` (default 1, stride)

---

## 📁 Section 4: 05_Strings — Manipulation, Slicing & Methods

### Q11. Explain String Slicing: `string[start:stop:step]`

```
 Index (Positive):   0   1   2   3   4   5
 Character:        ' P   y   t   h   o   n '
 Index (Negative):  -6  -5  -4  -3  -2  -1
```

```python
s = "Python"
print(s[0:4])   # "Pyth" (index 0 to 3)
print(s[::-1])  # "nohtyP" (Reverse string!)
print(s[::2])   # "Pto" (Every 2nd character)
```

---

### Built-in String Methods Quick Catalog

| Category | Method | Description |
| :--- | :--- | :--- |
| **Case** | `.lower()`, `.upper()`, `.title()`, `.capitalize()`, `.swapcase()` | Converts casing of characters. |
| **Search** | `.find(sub)` (returns `-1` if absent), `.index(sub)` (raises `ValueError` if absent), `.count(sub)` | Finds substring locations and counts. |
| **Trim/Split** | `.strip()`, `.lstrip()`, `.rstrip()`, `.split(sep)`, `sep.join(list)`, `.replace(old, new)` | Cleans, splits, joins, and replaces strings. |
| **Check** | `.isalpha()`, `.isdigit()`, `.isalnum()`, `.isspace()`, `.isupper()`, `.islower()` | Boolean character validation checks. |

---

## 📁 Section 5: 06_Patterns — Nested Loop Logic

### Q12. How do Nested Loops create patterns?
**Answer:**
- **Outer Loop:** Controls the number of **Rows**.
- **Inner Loop:** Controls the number of **Columns / Symbols** per row.

```python
# Pyramid Pattern Example
n = 4
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

```
   *
  ***
 *****
*******
```

---

## 📁 Section 6: 07_Functions — Scope (LEGB), Arguments & Recursion

### Q13. What is the LEGB Scope Resolution Rule?
When searching for a variable name, Python looks in 4 nested scopes:

$$\text{Local (L)} \longrightarrow \text{Enclosing (E)} \longrightarrow \text{Global (G)} \longrightarrow \text{Built-in (B)}$$

```python
x = "Global"

def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print(x)  # Prints "Local"
    inner()
```

---

### Q14. `*args` vs `**kwargs`
- `*args`: Collects positional arguments into a **Tuple**.
- `**kwargs`: Collects keyword arguments into a **Dictionary**.

```python
def example(*args, **kwargs):
    print("Positional (Tuple):", args)
    print("Keyword (Dict):", kwargs)

example(1, 2, a=10, b=20)
# Positional (Tuple): (1, 2)
# Keyword (Dict): {'a': 10, 'b': 20}
```

---

### Q15. Higher-Order Functions & Lambda
- **`lambda args: expression`**: Anonymous single-line function.
- **`map(func, iterable)`**: Applies `func` to every item.
- **`filter(func, iterable)`**: Filters items where `func(item)` is `True`.

```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]
squares = list(map(lambda x: x**2, nums))          # [1, 4, 9, 16, 25]
```

---

## 📁 Section 7: 08_Collections — Lists, Tuples, Sets, Dicts & Algorithms

### Collections Comparison Matrix

| Collection | Syntax | Ordered | Mutable | Unique Only? | Primary Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **List** | `[1, 2]` | ✅ Yes | ✅ Yes | ❌ Duplicates ok | General ordered sequence. |
| **Tuple** | `(1, 2)` | ✅ Yes | ❌ No | ❌ Duplicates ok | Immutable fixed records. |
| **Set** | `{1, 2}` | ❌ No | ✅ Yes | ✅ Unique only | Fast membership & set operations. |
| **Dictionary**| `{"a": 1}`| ✅ Yes (3.7+)| ✅ Yes | Keys: Unique | Key-Value fast lookup ($O(1)$). |

---

### Q16. Why are Dictionary Lookups $O(1)$ Time Complexity?
**Answer:**
Dictionaries use **Hash Tables**. `hash(key)` directly maps the key to its exact memory slot address, allowing instant $O(1)$ access without scanning items sequentially.

---

### Method Cheat Sheet for Collections
- **List:** `.append()`, `.extend()`, `.insert()`, `.pop()`, `.remove()`, `.sort()`, `.reverse()`
- **Dict:** `.get(key, default)` (Safe lookup!), `.keys()`, `.values()`, `.items()`, `.update()`, `.pop()`
- **Set:** `.add()`, `.discard()` (Safe remove!), `.union()` (`|`), `.intersection()` (`&`), `.difference()` (`-`)

---

## 📁 Section 8: 09_Tasks — Special Numbers & Daily Problems

### 1. Armstrong Number
Sum of digits raised to the power of number of digits equals the original number.
$$\text{Example: } 153 \longrightarrow 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$$

### 2. Perfect Number
Sum of proper divisors (excluding itself) equals the original number.
$$\text{Example: } 6 \longrightarrow 1 + 2 + 3 = 6$$

### 3. Palindrome & Strong Numbers
- **Palindrome:** Read same forward and backward (`121`, `"madam"`).
- **Strong Number:** Sum of factorials of digits equals original number ($145 = 1! + 4! + 5!$).

---

## 📁 Section 9: 10_Exception_Handling — Errors & Exception Control

### Q17. How does `try...except...else...finally` work?
**Answer:**

```
          [ try Block ] (Runs risk code)
                │
        ┌───────┴───────┐
   (Exception?)      (No Exception?)
        │                   │
  [ except Block ]     [ else Block ]
  (Handles error)     (Runs if clean)
        └───────┬───────┘
                │
        [ finally Block ]
    (ALWAYS runs at end!)
```

```python
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid number input!")
else:
    print("Result:", result)      # Runs ONLY if no exception occurred
finally:
    print("Execution completed.") # ALWAYS runs (useful for cleanup)
```

---

### Q18. Custom Exceptions
Inherit from Python's built-in `Exception` class:

```python
class InsufficientBalanceError(Exception):
    pass

balance = 100
withdraw = 150
if withdraw > balance:
    raise InsufficientBalanceError("Balance is too low!")
```

---

## 📁 Section 10: 11_File_Handling — File I/O & Disk Operations

### Q19. How do File Open Modes and Context Managers work?
**Answer:**

```python
# Best Practice: Use 'with open()' — automatically closes file even if errors occur!
with open("sample.txt", "w") as file:
    file.write("Hello Python File Handling!\n")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

| Mode | Name | Description |
| :--- | :--- | :--- |
| **`"r"`** | Read | Opens for reading (default). Raises `FileNotFoundError` if file missing. |
| **`"w"`** | Write | Opens for writing. **Overwrites** existing file or creates new file. |
| **`"a"`** | Append | Opens for appending. Adds new content to **end** of file. |
| **`"r+"`**| Read/Write | Opens for both reading and writing. |

---

## 📁 Section 11: 12_OOPs — Object-Oriented Programming

### Q20. What are the 4 Pillars of Object-Oriented Programming (OOP)?
**Answer:**

```
                 +-----------------------------------+
                 | 🏛️ 4 Pillars of Python OOP         |
                 +-----------------------------------+
                 | 1. Encapsulation (Data Hiding)   |
                 | 2. Abstraction   (Hiding Complexity)|
                 | 3. Inheritance   (Code Reusability) |
                 | 4. Polymorphism  (Many Forms)     |
                 +-----------------------------------+
```

```python
class Animal:
    def __init__(self, name):
        self.name = name  # Instance Attribute
        self._private_tag = "Secret"  # Encapsulation (_protected)

    def speak(self):
        pass  # Abstraction

class Dog(Animal):  # Inheritance
    def speak(self):
        return f"{self.name} says Woof!"  # Polymorphism

class Cat(Animal):  # Inheritance
    def speak(self):
        return f"{self.name} says Meow!"  # Polymorphism

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!
```

---

## 📁 Section 12: Advanced Interview Concepts

### Q21. Shallow Copy vs Deep Copy
- **Shallow Copy (`copy.copy()`):** Duplicates outer container, but **shares references** to nested mutable objects.
- **Deep Copy (`copy.deepcopy()`):** Recursively duplicates **all nested objects**, creating a 100% independent twin.

---

### Q22. Memory Management & Garbage Collection
1. **Reference Counting:** Objects track how many pointers reference them. Dropping to `0` deallocates memory instantly.
2. **Generational Garbage Collector:** Collects **cyclic dead references** across 3 generations (Gen 0, Gen 1, Gen 2).

---

### Q23. What is the GIL (Global Interpreter Lock)?
A mutex lock in CPython ensuring **only one thread executes Python bytecode at a time**.
- ✅ Works great for **I/O-bound** multithreading (downloads, file reading).
- ❌ For **CPU-bound** multi-core parallelism, use `multiprocessing`.

---

### Q24. What is `if __name__ == "__main__":`?
Assigns `"__main__"` when a script runs directly, and `"module_name"` when imported. Prevents unwanted execution during library imports.
