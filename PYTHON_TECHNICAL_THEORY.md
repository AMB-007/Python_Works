# Comprehensive Python Technical Theory & Method Reference Guide with Examples

This guide contains complete theoretical explanations, concepts, built-in methods references, code examples for **every single topic**, and technical interview Q&As covering all 12 core Python domains.

---

## 1. Python Basics, Variables, Data Types & Operators

### Q1. What is Python and what are its key features?
**Answer:**
Python is a high-level, interpreted, dynamically-typed, and garbage-collected programming language that supports procedural, object-oriented, and functional paradigms.

```python
# Dynamically typed: Variable type determined at runtime
x = 10         # int
x = "Python"   # changed to str dynamically
print(type(x)) # Output: <class 'str'>
```

---

### Q2. How are built-in data types classified in Python?
**Answer:**
1. **Numeric Types:** `int`, `float`, `complex`
2. **Sequence Types:** `str`, `list`, `tuple`
3. **Mapping Type:** `dict`
4. **Set Types:** `set`, `frozenset`
5. **Boolean Type:** `bool` (`True`, `False`)
6. **None Type:** `NoneType` (`None`)

```python
num = 42             # int
pi = 3.14159         # float
c = 3 + 4j           # complex
is_active = True     # bool
data = None          # NoneType

print(type(num), type(pi), type(c), type(is_active), type(data))
```

---

### Q3. Explain Mutable vs. Immutable Data Types.
**Answer:**
- **Mutable:** Contents can be changed after creation without altering memory ID (`id()`). (*list, dict, set, bytearray*)
- **Immutable:** Contents **cannot** be changed in-place. Modification creates a new object in memory. (*int, float, str, tuple, frozenset, bool*)

```python
# Mutable example (List): ID remains same after mutation
lst = [1, 2, 3]
print("ID before:", id(lst))
lst.append(4)
print("ID after:", id(lst)) # Same ID!

# Immutable example (String): Reassignment creates NEW object ID
s = "hello"
print("ID before:", id(s))
s = s + " world"
print("ID after:", id(s))  # Different ID!
```

---

### Q4. Differentiate `/` (Float Division) vs. `//` (Floor Division).
**Answer:**
- `/`: Performs standard division and **always returns a float**.
- `//`: Performs floor division and rounds **down** to the nearest integer floor value.

```python
print(7 / 2)    # 3.5  (Float Division)
print(7 // 2)   # 3    (Floor Division)
print(-7 // 2)  # -4   (Rounds down towards negative infinity)
```

---

### Q5. What is Type Casting? Implicit vs. Explicit Type Casting.
**Answer:**
- **Implicit:** Automatically done by Python when combining compatible types.
- **Explicit:** Manually done by programmer using constructors (`int()`, `float()`, `str()`, `list()`).

```python
# Implicit casting
res = 5 + 2.5       # int (5) implicitly converted to float (5.0) -> 7.5
print(res, type(res))

# Explicit casting
num_str = "100"
num_int = int(num_str) # explicit string -> int conversion
print(num_int + 50)    # 150
```

---

### Q6. Modulus Operator `%` and its Applications.
**Answer:**
The modulus operator returns the division remainder. Used for even/odd checks, digit extraction, and cyclical bounds.

```python
n = 1234
print("Is even?:", n % 2 == 0)      # True
print("Last digit:", n % 10)         # 4
print("Cycle 0-2:", 5 % 3)           # 2
```

---

## 2. Decision Making & Control Flow

### Q7. Truth Value Testing & Falsey Values.
**Answer:**
The following evaluate to `False` in conditional contexts: `None`, `False`, `0`, `0.0`, `""`, `()`, `[]`, `{}`, `set()`. All others are `True`.

```python
items = []
if not items:
    print("List is empty (Falsey)")

name = "Arjun"
if name:
    print(f"Hello, {name} (Truthy)")
```

---

### Q8. Short-Circuit Evaluation (`and` / `or`).
**Answer:**
Python evaluates logical expressions left-to-right and stops as soon as the result is guaranteed.

```python
def check():
    print("Function called!")
    return True

# Short-circuiting 'or': first condition is True, check() is NEVER called
result = True or check()  # 'Function called!' is NOT printed
```

---

### Q9. Ternary Operator.
**Answer:**
Syntax: `value_if_true if condition else value_if_false`

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status) # Output: Adult
```

---

## 3. Loops, Iteration & Control Statements

### Q10. `break`, `continue`, and `pass`.
**Answer:**
- `break`: Exits the loop immediately.
- `continue`: Skips remainder of current iteration.
- `pass`: Null placeholder statement.

```python
# break example
for i in range(1, 10):
    if i == 4:
        break
    print(i, end=" ") # 1 2 3
print()

# continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ") # 1 2 4 5
print()
```

---

### Q11. `for...else` and `while...else`.
**Answer:**
The `else` block executes ONLY IF the loop completes naturally without hitting a `break`.

```python
for n in range(2, 5):
    if 7 % n == 0:
        print("Not Prime")
        break
else:
    print("7 is Prime (Loop completed without break)")
```

---

### Q12. `range()` function and lazy evaluation.
**Answer:**
`range(start, stop, step)` generates integers lazily on demand without loading everything in memory.

```python
r = range(1, 10, 2)
print(list(r)) # [1, 3, 5, 7, 9]
```

---

## 4. Strings: Theory, Slicing & All Built-in String Methods

### Q13. String Immutability & Slicing `[start:stop:step]`.
```python
s = "Python Programming"
print(s[0:6])    # 'Python'
print(s[::-1])   # 'gnimmargorP nohtyP' (Reversed)
print(s[::2])    # 'Pto rgamn'
```

---

### Complete String Methods with Code Examples

```python
s = "  hello world  "

# A. Case Conversion Methods
print("hello".upper())        # 'HELLO'
print("HELLO".lower())        # 'hello'
print("hello world".title())  # 'Hello World'
print("hello world".capitalize()) # 'Hello world'
print("Hello".swapcase())     # 'hELLO'

# B. Search & Inspection Methods
text = "python programming"
print(text.find("pro"))       # 7
print(text.find("java"))      # -1 (Not found)
print(text.index("pro"))      # 7 (Raises ValueError if missing)
print(text.count("o"))        # 2
print(text.startswith("py"))  # True
print(text.endswith("ing"))   # True

# C. Character Classification / Boolean Checking Methods
print("12345".isdigit())      # True
print("abcDE".isalpha())      # True
print("abc12".isalnum())      # True
print("   ".isspace())        # True
print("hello".islower())      # True
print("HELLO".isupper())      # True

# D. Trimming, Splitting & Joining Methods
print("  hello  ".strip())    # 'hello'
print("apple,banana,orange".split(",")) # ['apple', 'banana', 'orange']
print("-".join(["2026", "07", "31"]))   # '2026-07-31'
print("Hello World".replace("World", "Python")) # 'Hello Python'
print("123".zfill(6))         # '000123'
```

---

## 5. Functions, Scope (LEGB), Arguments & Recursion

### Q14. LEGB Scope Resolution Rule.
```python
x = "Global"

def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print("Inner x:", x)
    inner()

outer() # Output: Inner x: Local
```

---

### Q15. `*args` and `**kwargs`.
```python
def demo_args_kwargs(required, *args, **kwargs):
    print("Required:", required)
    print("args (tuple):", args)
    print("kwargs (dict):", kwargs)

demo_args_kwargs("main", 10, 20, 30, user="Arjun", role="Dev")
```

---

### Q16. Recursion & Base Case.
```python
def factorial(n):
    if n <= 1:          # BASE CASE
        return 1
    return n * factorial(n - 1) # RECURSIVE CASE

print("5! =", factorial(5)) # 120
```

---

### Q17. Lambda Functions.
```python
square = lambda x: x ** 2
add = lambda a, b: a + b

print(square(6)) # 36
print(add(10, 20)) # 30
```

---

## 6. Collections (Lists, Tuples, Sets, Dictionaries) & Method References

### Comparison Table
| Property | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Syntax | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"a": 1}` |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys: No, Values: Yes |

---

### List Methods with Code Examples
```python
lst = [10, 20, 30]
lst.append(40)               # [10, 20, 30, 40]
lst.extend([50, 60])         # [10, 20, 30, 40, 50, 60]
lst.insert(1, 15)            # [10, 15, 20, 30, 40, 50, 60]
lst.remove(20)               # Removes first 20
popped = lst.pop()           # Removes & returns last item (60)
lst.sort(reverse=True)       # Sorts descending
lst.reverse()                # Reverses in-place
print("Final List:", lst)
```

---

### Dictionary Methods with Code Examples
```python
student = {"name": "Arjun", "age": 21}
print(student.get("score", 0)) # 0 (Safe get, no KeyError)

student.update({"age": 22, "grade": "A"})
print(student.keys())    # dict_keys(['name', 'age', 'grade'])
print(student.values())  # dict_values(['Arjun', 22, 'A'])
print(student.items())   # dict_items([('name', 'Arjun'), ...])

removed_age = student.pop("age")
print("Remaining Dict:", student)
```

---

### Set Methods with Code Examples
```python
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

setA.add(99)
setA.discard(99) # Safe removal (No KeyError if missing)

print("Union (|):", setA | setB)                # {1, 2, 3, 4, 5, 6}
print("Intersection (&):", setA & setB)         # {3, 4}
print("Difference (-):", setA - setB)           # {1, 2}
print("Symmetric Diff (^):", setA ^ setB)       # {1, 2, 5, 6}
```

---

## 7. Useful Built-in Functions & Math Module

```python
import math

nums = [5, 2, 9, 1, 7]
print("len:", len(nums))
print("sum:", sum(nums))
print("max/min:", max(nums), min(nums))
print("sorted:", sorted(nums))

# zip and enumerate
names = ["Alice", "Bob"]
scores = [85, 90]
for idx, (name, score) in enumerate(zip(names, scores), 1):
    print(f"{idx}. {name}: {score}")

# Math module
print("sqrt(16):", math.sqrt(16))      # 4.0
print("ceil(4.2):", math.ceil(4.2))    # 5
print("floor(4.9):", math.floor(4.9))  # 4
print("gcd(12, 18):", math.gcd(12, 18))# 6
```

---

## 8. Exception Handling (`10_Exception_Handling`)

### Q18. How does `try-except-else-finally` work in Python?
**Answer:**
- `try`: Contains code that might raise an exception.
- `except`: Catches and handles specific exceptions.
- `else`: Runs ONLY IF no exception occurred in `try`.
- `finally`: ALWAYS runs regardless of whether an exception occurred or not (used for cleanup).

```python
try:
    num = int("10")
    res = 100 / num
except ValueError:
    print("Invalid integer string!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Success! Result = {res}")
finally:
    print("Cleanup & execution finished.")
```

---

### Q19. How to raise Custom Exceptions and use `assert`?
**Answer:**
- `raise`: Manually triggers an exception.
- `assert`: Tests a condition; if False, raises `AssertionError`.

```python
# Custom exception raise
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

# Assert example
def calculate_discount(price):
    assert price > 0, "Price must be positive!"
    return price * 0.9

print(calculate_discount(100)) # 90.0
```

---

## 9. File Handling (`11_File_Handling`)

### Q20. File Modes & Context Manager (`with` statement).
**Answer:**
Modes: `'r'` (read), `'w'` (write/overwrite), `'a'` (append), `'b'` (binary).  
`with open(...) as f:` automatically closes the file even if exceptions occur.

```python
# Writing to a file using 'with'
with open("sample_file.txt", "w") as file:
    file.write("Hello, World!\nWelcome to File Handling.")

# Reading file methods: .read(), .readline(), .readlines()
with open("sample_file.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Handling FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Error: The requested file was not found!")
```

---

## 10. Object-Oriented Programming - OOPs (`12_OOPs`)

### Q21. Classes, Objects, and `__init__()` Constructor.
**Answer:**
- **Class:** Blueprint for creating objects.
- **Object:** Instance of a class.
- `__init__()`: Initializer method called automatically when creating an object.

```python
class Student:
    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age

    def display(self):  # Instance method
        return f"Student: {self.name}, Age: {self.age}"

s1 = Student("Arjun", 21)
print(s1.display())
```

---

### Q22. The 4 Pillars of OOPs: Encapsulation, Inheritance, Polymorphism, Abstraction.

#### 1. Encapsulation (Private / Public Members)
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private attribute (starts with __)

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance()) # 1500
```

#### 2. Inheritance (Single & Multilevel)
```python
class Parent:
    def speak(self):
        return "Parent speaking"

class Child(Parent): # Inheritance
    def play(self):
        return "Child playing"

c = Child()
print(c.speak()) # Inherited from Parent
print(c.play())
```

#### 3. Polymorphism (Method Overriding & Overloading)
```python
# Method Overriding
class Animal:
    def make_sound(self):
        return "Generic sound"

class Dog(Animal):
    def make_sound(self): # Overrides parent method
        return "Woof Woof!"

dog = Dog()
print(dog.make_sound()) # Woof Woof!
```

#### 4. Abstraction (`abc.ABC` & `@abstractmethod`)
```python
from abc import ABC, abstractmethod

class Shape(ABC): # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self): # Must implement abstract method
        return self.side ** 2

sq = Square(4)
print("Square Area:", sq.area()) # 16
```

---

## 11. Algorithms & Special Number Logic

```python
# A. Armstrong Number
def is_armstrong(n):
    s = str(n)
    p = len(s)
    return sum(int(d) ** p for d in s) == n

print("Is 153 Armstrong?:", is_armstrong(153)) # True

# B. Binary Search (O(log N))
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("Binary Search index:", binary_search([10, 20, 30, 40, 50], 40)) # 3
```

---

## 12. Advanced Python Interview Concepts

### Q23. Shallow Copy vs. Deep Copy.
```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 999
print("Original:", original) # [[999, 2], [3, 4]]
print("Shallow:", shallow)   # [[999, 2], [3, 4]] (Affected)
print("Deep:", deep)         # [[1, 2], [3, 4]]    (Unaffected)
```

---

### Q24. Memory Management & Reference Counting.
**Answer:**
Python manages memory using:
1. **Reference Counting:** Objects track how many references point to them. When references drop to 0, memory is freed immediately.
2. **Generational Garbage Collection (GC):** Handles cyclic references across Gen 0, Gen 1, and Gen 2.

---

### Q25. What is `__name__ == "__main__"`?
```python
if __name__ == "__main__":
    print("This script is running directly as the main program.")
```
