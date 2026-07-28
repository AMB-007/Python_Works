# 📘 Master Python Technical Reference & Theory Guide

> **Complete Comprehensive Reference:** This guide covers **all technical concepts, syntax rules, methods, formulas, algorithms, and code examples** corresponding to every file and folder in the `Python_Works` workspace (`01_Basics` ➔ `12_OOPs`).

---

## 🧭 Master Folder & Topic Index

```
Python_Works/
├── 📁 01_Basics               ➔ Execution, Variables, Calculations, Conversions, Operators
├── 📁 02_Decision_Making      ➔ If-Else, Logical Operators, Nested-If, Ternary Operator
├── 📁 03_While_Loops          ➔ While iteration, Number reversals, Digit math, Special numbers
├── 📁 04_For_Loops            ➔ For iteration, range(), Prime checks, Factorials, Range series
├── 📁 05_Strings              ➔ Slicing, Casing, Search/Frequency, Validation methods
├── 📁 06_Patterns             ➔ Grid logic, Star pyramids, Inverted triangles, Exam patterns
├── 📁 07_Functions            ➔ LEGB Scope, *args/**kwargs, Lambda, Map/Filter/Reduce, Recursion
├── 📁 08_Collections          ➔ List, Dict, Set, Tuple, Hash Tables, Comprehensions, Search/Sort
├── 📁 09_Tasks                ➔ Daily challenge algorithms & special number formulas
├── 📁 10_Exception_Handling   ➔ try/except/else/finally, Built-in errors, Assertions, Custom errors
├── 📁 11_File_Handling        ➔ Disk I/O, File modes, Read/Write methods, Context managers
└── 📁 12_OOPs                 ➔ Classes, __init__, self, Encapsulation, Inheritance, Polymorphism
```

---

## 📁 1. 01_Basics — Core Architecture, Variables & Operators

### 1.1 Python Architecture & Code Execution
Python uses a 2-stage execution model:

```
[ Source (.py) ] ──> ( Python Compiler ) ──> [ Bytecode (.pyc) ] ──> ( PVM Interpreter ) ──> [ CPU Execution ]
```

1. **Compilation Phase:** Translates `.py` source code into intermediate **Bytecode** (`.pyc`).
2. **Interpretation Phase:** The **Python Virtual Machine (PVM)** executes bytecode line-by-line.

---

### 1.2 Variables & Memory Allocation Model
In Python, variables are **labels (pointers)** to objects stored in memory.

```python
x = 10
y = 10
# Both x and y point to the exact same memory address!
print(id(x) == id(y))  # Output: True
```

---

### 1.3 Data Types & Mutability Classification
- **Immutable Types:** State **cannot** be altered in-place. Modifying creates a new memory object.  
  `int`, `float`, `complex`, `str`, `tuple`, `bool`, `frozenset`, `bytes`
- **Mutable Types:** State **can** be altered in-place (`id()` remains unchanged).  
  `list`, `dict`, `set`, `bytearray`

```python
# Modifying a list in-place (Mutable)
nums = [1, 2]
print(id(nums))        # Memory Address A
nums.append(3)
print(id(nums))        # Memory Address A (Unchanged!)

# Modifying a string (Immutable)
text = "Hello"
print(id(text))        # Memory Address B
text += " World"
print(id(text))        # Memory Address C (New Object Created!)
```

---

### 1.4 Arithmetic, Conversions & Financial Calculations

#### A. Division Operators
```python
print(7 / 2)   # Float Division  -> 3.5 (Always returns float)
print(7 // 2)  # Floor Division  -> 3   (Rounds down to integer)
print(-7 // 2) # Floor Division  -> -4  (Rounds down towards negative infinity)
print(7 % 2)   # Modulus         -> 1   (Remainder of division)
```

#### B. Key formulas from `Calculations/` & `Conversions/`
- **BMI (Body Mass Index):** `bmi = weight / (height ** 2)`
- **BMR (Basal Metabolic Rate):** `bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5`
- **Simple Interest:** `si = (principal * rate * time) / 100`
- **Celsius to Fahrenheit:** `f = (c * 9/5) + 32`
- **Days/Hours/Minutes/Seconds Conversion:**
  ```python
  total_sec = 90061
  days = total_sec // 86400
  hours = (total_sec % 86400) // 3600
  minutes = (total_sec % 3600) // 60
  seconds = total_sec % 60
  # Output: 1 Days, 1 Hours, 1 Minutes, 1 Seconds
  ```

#### C. Variable Swapping (`swap_two_no.py`)
```python
a, b = 5, 10
# Pythonic tuple unpacking swap (no temp variable required):
a, b = b, a
print(a, b)  # Output: 10, 5
```

---

## 📁 2. 02_Decision_Making — Branching & Boolean Logic

### 2.1 Conditional Branching (`if`, `elif`, `else`)
Executes code blocks based on condition evaluation.

```python
# ATM Machine Logic Example (from 02_Decision_Making/If_Else/atm_machine.py)
balance = 5000
withdraw = int(input("Enter amount: "))

if withdraw <= 0:
    print("Invalid amount!")
elif withdraw > balance:
    print("Insufficient funds!")
else:
    balance -= withdraw
    print(f"Withdrawal successful! Remaining balance: {balance}")
```

---

### 2.2 Truth Value Testing (Truthy vs. Falsy)
Python automatically converts conditions to boolean (`True` or `False`).

| Falsy Values (`False`) | Truthy Values (`True`) |
| :--- | :--- |
| `None`, `False` | `True` |
| Zeros: `0`, `0.0`, `0j` | Non-zero numbers: `1`, `-5`, `3.14` |
| Empty collections: `""`, `[]`, `()`, `{}`, `set()` | Non-empty collections: `"a"`, `[1]`, `{"k": "v"}` |

---

### 2.3 Short-Circuit Logic (`and`, `or`)
- **`A and B`**: If `A` is `False`, `B` is **skipped** (returns `False`).
- **`A or B`**: If `A` is `True`, `B` is **skipped** (returns `True`).

```python
# Divisible by both 3 and 5 (from Logical_Operators/divisible_by_3_and_5.py)
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
```

---

### 2.4 Ternary Conditional Operator
**Syntax:** `true_value if condition else false_value`

```python
num = 7
result = "Even" if num % 2 == 0 else "Odd"  # Output: "Odd"
```

---

## 📁 3. 03_While_Loops — Indefinite Iteration & Digit Mathematics

### 3.1 Loop Architecture & Controls
```python
# Syntax:
# while condition:
#     statement_block

# Loop Statements:
# break    -> Terminate loop immediately
# continue -> Skip to next iteration
# pass     -> Placeholder statement (no-op)
```

---

### 3.2 Digit Extraction & Number Manipulation
Common digit-processing patterns used in `Number_Problems/`:

```python
n = 1234
digit_sum = 0
rev = 0

while n > 0:
    rem = n % 10        # 1. Extract last digit
    digit_sum += rem    # 2. Add to sum
    rev = rev * 10 + rem# 3. Build reversed number
    n //= 10            # 4. Remove last digit

# Output: digit_sum = 10, rev = 4321
```

---

### 3.3 `while...else` Construct
Runs the `else` block **only when loop exits naturally** (without `break`).

```python
# Guessing Game (from 03_While_Loops/Number_Problems/guess_number_game.py)
secret = 7
attempts = 3

while attempts > 0:
    guess = int(input("Guess number: "))
    if guess == secret:
        print("You won!")
        break
    attempts -= 1
else:
    print("Out of attempts! You lost.")  # Executes if while loop finishes naturally
```

---

## 📁 4. 04_For_Loops — Definite Iteration, Sequences & Ranges

### 4.1 `range()` Syntax & Performance
Generates integer sequences lazily ($O(1)$ memory usage).  
**Syntax:** `range(start, stop, step)`  
*(Note: `start` is inclusive, `stop` is exclusive).*

```python
for i in range(10, 0, -2):
    print(i, end=" ")  # Output: 10 8 6 4 2
```

---

### 4.2 Prime Number & Range Algorithms

```python
# Checking if a number is Prime (from 04_For_Loops/Special_Numbers/prime.py)
n = 29
is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")  # Output: Prime
```

---

## 📁 5. 05_Strings — Manipulation, Slicing & Complete Method Catalog

### 5.1 String Slicing Syntax
**Syntax:** `string[start:stop:step]`

```python
s = "PythonProgramming"

print(s[0:6])     # "Python"      (Index 0 to 5)
print(s[6:])      # "Programming" (Index 6 to end)
print(s[::-1])    # "gnimmargorPnohtyP" (Reverse string)
print(s[::2])     # "PtoPgamn"    (Step size of 2)
```

---

### 5.2 Complete Built-in String Methods Reference

#### A. Case Conversion
```python
s = "hello World"
print(s.lower())      # "hello world"
print(s.upper())      # "HELLO WORLD"
print(s.title())      # "Hello World"
print(s.capitalize()) # "Hello world"
print(s.swapcase())   # "HELLO wORLD"
```

#### B. Inspection & Searching
```python
s = "banana"
print(s.count("a"))      # 3
print(s.find("a"))       # 1  (Returns -1 if not found)
print(s.rfind("a"))      # 5  (Rightmost index)
print(s.index("a"))      # 1  (Raises ValueError if not found)
print(s.startswith("b")) # True
print(s.endswith("a"))   # True
```

#### C. Validation (Boolean Checks)
```python
"123".isdigit()   # True
"abc".isalpha()   # True
"a12".isalnum()   # True
"   ".isspace()   # True
"abc".islower()   # True
"ABC".isupper()   # True
```

#### D. Trimming, Splitting & Joining
```python
s = "  python  "
print(s.strip())         # "python" (Removes leading & trailing whitespace)
print(s.lstrip())        # "python  "
print(s.rstrip())        # "  python"

csv = "apple,banana,orange"
fruits = csv.split(",")  # ['apple', 'banana', 'orange']
joined = "-".join(fruits)# "apple-banana-orange"

print("cat".replace("c", "b")) # "bat"
```

---

## 📁 6. 06_Patterns — Nested Loops & Pattern Logic

### 6.1 Logic Structure for Pattern Grids
- **Outer Loop (`i`):** Manages **Row index** ($1 \dots N$).
- **Inner Loop (`j`):** Manages **Spaces and Characters/Stars per row**.

```python
# Star Pyramid (from 06_Patterns/star_patterns.py)
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

```
    *
   ***
  *****
 *******
*********
```

```python
# Number Pattern Grid (from 06_Patterns/patterns.py)
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

---

## 📁 7. 07_Functions — Scope, Positional/Keyword Args, Lambda & Recursion

### 7.1 LEGB Scope Resolution Order
Python resolves variable names in 4 nested scopes:

$$\text{Local (L)} \longrightarrow \text{Enclosing (E)} \longrightarrow \text{Global (G)} \longrightarrow \text{Built-in (B)}$$

```python
x = "Global"

def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print(x) # Output: "Local"
    inner()

outer()
```

---

### 7.2 Variable Arguments: `*args` and `**kwargs`
- **`*args`**: Packs arbitrary positional arguments into a **Tuple**.
- **`**kwargs`**: Packs arbitrary keyword arguments into a **Dictionary**.

```python
def flexi_func(*args, **kwargs):
    print("Args (Tuple):", args)
    print("Kwargs (Dict):", kwargs)

flexi_func(1, 2, 3, name="Alice", age=25)
# Output:
# Args (Tuple): (1, 2, 3)
# Kwargs (Dict): {'name': 'Alice', 'age': 25}
```

---

### 7.3 Lambda & Higher-Order Functions (`map`, `filter`, `reduce`)

```python
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# 1. Lambda (Anonymous function)
square = lambda x: x**2

# 2. Filter (Extracts elements where condition is True)
evens = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4, 6]

# 3. Map (Transforms every element)
doubled = list(map(lambda x: x * 2, nums))       # [2, 4, 6, 8, 10, 12]

# 4. Reduce (Accumulates elements into a single value)
total_sum = reduce(lambda acc, x: acc + x, nums) # 21
```

---

### 7.4 Recursion & Base Case
A function calling itself must have a **Base Case** to stop infinite calls and prevent `RecursionError` (Stack Overflow).

```python
# Recursive Factorial (from 07_Functions/Recursion/recursive_factorial.py)
def factorial(n):
    if n == 0 or n == 1: # Base Case
        return 1
    return n * factorial(n - 1) # Recursive Case

print(factorial(5)) # Output: 120
```

---

## 📁 8. 08_Collections — Lists, Dictionaries, Sets, Tuples & Algorithms

### 8.1 Comparison Matrix

| Property | List (`[]`) | Tuple (`()`) | Set (`{}`) | Dictionary (`{k: v}`) |
| :--- | :--- | :--- | :--- | :--- |
| **Ordering** | Ordered | Ordered | Unordered | Key-ordered (3.7+) |
| **Mutability** | Mutable | Immutable | Mutable | Mutable |
| **Duplicates** | Allowed | Allowed | Unique Only | Unique Keys |
| **Indexing** | `lst[i]` | `tup[i]` | No indexing | `dict[key]` |

---

### 8.2 Complete Method References

#### A. List Methods (`List_Operations/`)
- `lst.append(x)` — Adds `x` to end.
- `lst.extend(iterable)` — Appends all items from iterable.
- `lst.insert(i, x)` — Inserts `x` at index `i`.
- `lst.remove(x)` — Removes first occurrence of `x`.
- `lst.pop([i])` — Removes & returns element at index `i` (default last).
- `lst.sort(key=None, reverse=False)` — Sorts **in-place**.
- `lst.reverse()` — Reverses list **in-place**.

#### B. Dictionary Methods (`Dictionaries/`)
- `d.get(key, default=None)` — Returns value safely without raising `KeyError`.
- `d.keys()`, `d.values()`, `d.items()` — View objects for keys, values, and `(k, v)` tuples.
- `d.update(other_dict)` — Merges key-values from another dict.
- `d.pop(key)` — Removes `key` and returns its value.

#### C. Set Operations (`Set`)
- `s1.union(s2)` (`s1 | s2`) — Elements in either set.
- `s1.intersection(s2)` (`s1 & s2`) — Elements in BOTH sets.
- `s1.difference(s2)` (`s1 - s2`) — Elements in `s1` but NOT `s2`.
- `s1.symmetric_difference(s2)` (`s1 ^ s2`) — Elements in either set, but not both.

---

### 8.3 List Comprehension Syntax
**Syntax:** `[expression for item in iterable if condition]`

```python
# List of squares for even numbers 1..10
squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# Output: [4, 16, 36, 64, 100]
```

---

### 8.4 Searching & Sorting Algorithms

#### A. Linear Search vs. Binary Search
- **Linear Search:** Checks items one by one. Time Complexity: $O(N)$.
- **Binary Search:** Operates on **sorted arrays**, halving search space. Time Complexity: $O(\log N)$.

```python
# Binary Search Implementation
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
```

#### B. Second Largest Finding Algorithm (`second_largest.py`)
```python
def find_second_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

print(find_second_largest([12, 35, 1, 10, 34, 1]))  # Output: 34
```

---

## 📁 9. 09_Tasks — Special Number Formulas & Math Logic

| Special Number | Mathematical Definition | Example |
| :--- | :--- | :--- |
| **Armstrong Number** | $n$-digit number equal to the sum of digits raised to $n$-th power. | $153 = 1^3 + 5^3 + 3^3$ |
| **Perfect Number** | Equal to sum of all its proper divisors (excluding itself). | $6 = 1 + 2 + 3$ |
| **Palindrome** | Reads the same forwards and backwards. | $121$, `"madam"` |
| **Strong Number** | Equal to sum of factorials of its digits. | $145 = 1! + 4! + 5!$ |
| **Harshad Number** | Number divisible by the sum of its digits. | $18 \rightarrow 18 \% (1+8) == 0$ |
| **Automorphic Number**| Number whose square ends in the same digits as the number itself. | $25^2 = 625$ (ends in 25) |
| **Spy Number** | Sum of digits equals product of digits. | $1124 \rightarrow (1+1+2+4) == (1*1*2*4)$ |

---

## 📁 10. 10_Exception_Handling — Errors, Assertions & Custom Exceptions

### 10.1 `try...except...else...finally` Architecture

```
          [ try Block ] (Risky code)
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
    num = int("10")
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid string to integer conversion!")
else:
    print(f"Success! Result: {result}")
finally:
    print("Cleanup: Execution completed.")
```

---

### 10.2 Common Built-in Exceptions

- **`ZeroDivisionError`**: Division or modulo by zero (`5 / 0`).
- **`IndexError`**: Accessing sequence index out of bounds (`lst[99]`).
- **`KeyError`**: Accessing missing dictionary key (`dict["missing"]`).
- **`ValueError`**: Function receives argument of right type but inappropriate value (`int("abc")`).
- **`TypeError`**: Operation applied to inappropriate data type (`"5" + 5`).
- **`FileNotFoundError`**: Attempting to open non-existent disk file.

---

### 10.3 Assertions & Custom Exceptions

```python
# 1. Assertion (from 10_Exception_Handling/assert_error_handling.py)
age = -5
assert age >= 0, "Age cannot be negative!"  # Raises AssertionError if False

# 2. Custom Exception (from 10_Exception_Handling/custom_exception_raise.py)
class InvalidAgeError(Exception):
    pass

def check_voter(age):
    if age < 18:
        raise InvalidAgeError("Must be 18 or older to vote!")
```

---

## 📁 11. 11_File_Handling — File I/O, File Modes & Context Managers

### 11.1 File Modes Matrix

| Mode | Name | Behavior | Creates File if Missing? | Truncates (Clears) File? |
| :--- | :--- | :--- | :--- | :--- |
| **`"r"`** | Read | Opens for reading. (Default) | ❌ (Raises `FileNotFoundError`) | ❌ No |
| **`"w"`** | Write | Opens for writing. | ✅ Yes | ✅ Yes (Overwrites file) |
| **`"a"`** | Append | Opens for appending at file end. | ✅ Yes | ❌ No |
| **`"r+"`**| Read/Write | Opens for reading and writing. | ❌ (Raises `FileNotFoundError`) | ❌ No |

---

### 11.2 Reading & Writing Methods (`file_read_methods.py`)

```python
# Context Manager 'with open()' automatically handles file closure:
with open("sample.txt", "w") as f:
    f.write("Line 1: Python\nLine 2: File Handling\n")

with open("sample.txt", "r") as f:
    print(f.read())       # Reads ENTIRE file content as a single string
    
with open("sample.txt", "r") as f:
    print(f.readline())   # Reads a SINGLE line ending with \n

with open("sample.txt", "r") as f:
    print(f.readlines())  # Reads ALL lines into a List of strings ['Line 1...\n', ...]
```

---

### 11.3 File Exception Safe Handling (`file_read_exception.py`)

```python
try:
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: The requested file does not exist on disk!")
```

---

## 📁 12. 12_OOPs — Object-Oriented Programming Principles

### 12.1 Classes, Objects, `__init__` & `self`
- **Class:** Blueprint / template for creating objects.
- **Object:** Instance of a class stored in memory.
- **`__init__`:** Constructor method executed automatically on object creation.
- **`self`:** Reference to the current instance of the class.

```python
class Student:
    # Class Attribute (Shared by all instances)
    school_name = "Tech Academy"

    def __init__(self, name, age):
        # Instance Attributes (Unique to each instance)
        self.name = name
        self.age = age

    # Instance Method
    def display_info(self):
        return f"Student: {self.name}, Age: {self.age}, School: {self.school_name}"

s1 = Student("Alice", 20)
print(s1.display_info())
```

---

### 12.2 The 4 Pillars of OOP

```
               +-----------------------------------+
               | 🏛️ 4 Pillars of Python OOP         |
               +-----------------------------------+
               | 1. Encapsulation (Data Hiding)   |
               | 2. Abstraction   (Hiding Detail)  |
               | 3. Inheritance   (Code Reuse)     |
               | 4. Polymorphism  (Overriding)     |
               +-----------------------------------+
```

#### A. Encapsulation (Access Modifiers)
- **Public:** `self.name` (Accessible everywhere).
- **Protected:** `self._bank_code` (Prefix `_`, convention for subclass access).
- **Private:** `self.__pin` (Prefix `__`, triggers name mangling `_ClassName__pin`).

#### B. Inheritance
Child class inherits attributes and methods from Parent class using `super()`.

#### C. Polymorphism (Method Overriding)
Subclasses provide custom implementations of methods defined in their parent class.

#### D. Abstraction
Abstract Base Classes (`abc.ABC`) enforce method implementations in child classes.

```python
from abc import ABC, abstractmethod

# Abstraction
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Inheritance & Polymorphism
class Car(Vehicle):
    def start_engine(self):
        return "Car engine started with key ignition!"

class ElectricBike(Vehicle):
    def start_engine(self):
        return "Electric bike powered on silently!"

vehicles = [Car(), ElectricBike()]
for v in vehicles:
    print(v.start_engine())  # Polymorphic method call
```

---

## 📁 13. Advanced Python Interview Concepts

### 13.1 Shallow Copy vs. Deep Copy

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow Copy: Copies container, but shares nested references!
shallow = copy.copy(original)

# Deep Copy: Recursively duplicates ALL nested container objects!
deep = copy.deepcopy(original)

original[0][0] = 999
print(shallow[0][0])  # 999 (Affected by change!)
print(deep[0][0])     # 1   (Unchanged, independent memory copy!)
```

---

### 13.2 Memory Management & Garbage Collector (GC)
1. **Reference Counting:** Every object tracks how many references point to it. When count reaches `0`, memory is instantly deallocated.
2. **Generational Garbage Collector:** Collects **cyclic references** (e.g., Object A pointing to Object B and Object B pointing back to A) across 3 generations (Gen 0, Gen 1, Gen 2).

---

### 13.3 GIL (Global Interpreter Lock)
A mutex in CPython that restricts execution of Python bytecodes to a **single thread at a time**.
- ✅ Useful for **I/O-bound** multithreading (networking, file reads).
- ❌ For multi-core **CPU-bound** speedups, use `multiprocessing`.

---

### 13.4 `if __name__ == "__main__":`
Built-in variable `__name__` evaluates to `"__main__"` when a script is executed directly from terminal, but evaluates to module name when imported into another script.
