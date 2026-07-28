# Comprehensive Python Technical Theory & Method Reference Guide

This guide contains complete theoretical explanations, concepts, built-in methods references, and technical interview Q&As covering all areas of Python.

---

## 1. Python Basics, Variables, Data Types & Operators

### Q1. What is Python and what are its key features?
**Answer:**
Python is a high-level, interpreted, dynamically-typed, and garbage-collected programming language that supports multiple programming paradigms (procedural, object-oriented, functional).
Key Features:
- **Easy to read & learn:** Clean syntax emphasizing code readability.
- **Interpreted:** Executed line-by-line via Python Virtual Machine (PVM).
- **Dynamically Typed:** Variable types are determined at runtime.
- **Extensive Standard Library:** Built-in batteries included.

---

### Q2. How are built-in data types classified in Python?
**Answer:**
Python data types are broadly classified into:
1. **Numeric Types:** `int`, `float`, `complex`
2. **Sequence Types:** `str` (String), `list` (List), `tuple` (Tuple)
3. **Mapping Type:** `dict` (Dictionary)
4. **Set Types:** `set`, `frozenset`
5. **Boolean Type:** `bool` (`True`, `False`)
6. **Binary Types:** `bytes`, `bytearray`, `memoryview`
7. **None Type:** `NoneType` (`None`)

---

### Q3. Explain the difference between Mutable and Immutable data types.
**Answer:**
- **Mutable:** Objects whose state or contents can be changed after creation without changing their memory ID (`id()`).
  - *Examples:* `list`, `dict`, `set`, `bytearray`.
- **Immutable:** Objects whose state or contents **cannot** be changed once created. Any modification creates a new object in memory.
  - *Examples:* `int`, `float`, `str`, `tuple`, `frozenset`, `bool`.

---

### Q4. Differentiate between `/` (Float Division) and `//` (Floor Division).
**Answer:**
- `/` (Single Slash): Performs standard division and **always returns a `float`**.
  - Example: `7 / 2 -> 3.5`
- `//` (Double Slash): Performs floor division, which divides and rounds **down** to the nearest whole integer floor value.
  - Example: `7 // 2 -> 3`
  - Example: `-7 // 2 -> -4` (rounds down towards negative infinity)

---

### Q5. What is Type Casting? Differentiate Implicit vs. Explicit Type Casting.
**Answer:**
Type casting is the process of converting a value from one data type to another.
- **Implicit Conversion:** Automatically performed by Python when mixing compatible data types to prevent data loss.
  - Example: Adding an `int` and a `float` produces a `float` (`5 + 2.0 -> 7.0`).
- **Explicit Conversion:** Manually performed by the programmer using built-in constructor functions.
  - Examples: `int("10")`, `float(5)`, `str(100)`, `list((1, 2, 3))`.

---

### Q6. What does the `%` (Modulus) operator do, and where is it used?
**Answer:**
The modulus operator (`%`) returns the **remainder** of division between two numbers.
Common Uses:
1. **Even/Odd Check:** `number % 2 == 0`
2. **Extracting Digits:** `last_digit = number % 10`
3. **Cyclic Boundaries:** `index % max_size`

---

## 2. Decision Making & Control Flow

### Q7. How does Truth Value Testing work in Python? Which values evaluate to `False`?
**Answer:**
Any object in Python can be evaluated in a boolean conditional context (`if` or `while`).
The following values evaluate to `False` (Falsey values):
- `None` and `False`
- Numeric zeros: `0`, `0.0`, `0j`
- Empty collections & sequences: `""`, `()`, `[]`, `{}`, `set()`, `range(0)`
All other values evaluate to `True` (Truthy values).

---

### Q8. What is Short-Circuit Evaluation in Python?
**Answer:**
Short-circuiting means Python evaluates logical expressions (`and`, `or`) from left to right and stops evaluation as soon as the outcome is guaranteed:
- **`and` Operator:** If the first condition is `False`, Python immediately returns `False` without evaluating the remaining expressions.
- **`or` Operator:** If the first condition is `True`, Python immediately returns `True` without evaluating the remaining expressions.

---

### Q9. What is the Ternary Operator in Python and what is its syntax?
**Answer:**
The ternary operator (conditional expression) allows evaluating a condition in a single line.
**Syntax:** `value_if_true if condition else value_if_false`  
**Example:** `result = "Adult" if age >= 18 else "Minor"`

---

## 3. Loops, Iteration & Control Statements

### Q10. What is the difference between `break`, `continue`, and `pass`?
**Answer:**
- **`break`:** Exits and terminates the innermost loop immediately. Execution moves to the statement following the loop.
- **`continue`:** Skips the remainder of the current loop iteration and jumps immediately to the next iteration.
- **`pass`:** A null placeholder statement. It does nothing and is used when syntactical structure requires a block of code but no action is needed.

---

### Q11. Explain `for...else` and `while...else` in Python.
**Answer:**
In Python, loops can have an optional `else` block.
- The `else` block executes **only if the loop completes all iterations normally** without encountering a `break` statement.
- If a `break` statement prematurely exits the loop, the `else` block is **skipped**.

---

### Q12. How does `range()` work in Python?
**Answer:**
`range(start, stop, step)` creates an immutable sequence of integers:
- `start` (optional, default 0): Inclusive starting value.
- `stop` (required): Exclusive ending value.
- `step` (optional, default 1): Increment step size.
**Memory Efficiency:** `range()` generates numbers lazily on demand rather than allocating memory for an entire list at once.

---

## 4. Strings: Theory, Slicing & All Built-in String Methods

### Q13. Why are Python strings immutable?
**Answer:**
Strings cannot be altered in-place after creation due to:
1. **Security & Hashability:** Immutable strings allow computing a fixed hash code, enabling them to serve as dictionary keys and set elements.
2. **String Interning & Memory Optimization:** Identical string literals share the same memory location, saving memory.
3. **Thread Safety:** Immutable objects can be accessed across multiple threads without lock synchronization issues.

---

### Q14. Explain String Slicing syntax `string[start:stop:step]`.
**Answer:**
Slicing extracts a substring from a sequence:
- `start`: Index where slice begins (inclusive).
- `stop`: Index where slice ends (exclusive).
- `step`: Direction and stride of slicing.
Key Slicing Operations:
- `s[::-1]`: Reverses string (step is `-1`).
- `s[::2]`: Extracts every 2nd character.
- `s[1:4]`: Extracts characters at index 1, 2, and 3.

---

### Complete Built-in String Methods Reference

#### A. Case Conversion Methods
- **`s.lower()`**: Converts all characters in string to lowercase.  
  - *Example:* `"Hello".lower() -> "hello"`
- **`s.upper()`**: Converts all characters in string to uppercase.  
  - *Example:* `"hello".upper() -> "HELLO"`
- **`s.title()`**: Converts the first character of each word to uppercase and remaining to lowercase.  
  - *Example:* `"hello world".title() -> "Hello World"`
- **`s.capitalize()`**: Converts only the very first character of the string to uppercase.  
  - *Example:* `"hello world".capitalize() -> "Hello world"`
- **`s.swapcase()`**: Swaps uppercase characters to lowercase and vice versa.  
  - *Example:* `"Hello".swapcase() -> "hELLO"`
- **`s.casefold()`**: Stronger lowercase conversion designed for caseless Unicode comparisons.

#### B. Search & Inspection Methods
- **`s.find(sub[, start[, end]])`**: Returns the lowest index where substring `sub` is found. Returns `-1` if not found.
- **`s.rfind(sub)`**: Returns the highest (rightmost) index of substring `sub`, or `-1` if not found.
- **`s.index(sub)`**: Like `find()`, but raises a `ValueError` if substring is not found.
- **`s.rindex(sub)`**: Like `rfind()`, but raises a `ValueError` if substring is not found.
- **`s.count(sub)`**: Returns the total number of non-overlapping occurrences of substring `sub`.
- **`s.startswith(prefix)`**: Returns `True` if string starts with specified prefix; else `False`.
- **`s.endswith(suffix)`**: Returns `True` if string ends with specified suffix; else `False`.

#### C. Character Classification / Boolean Checking Methods
- **`s.isalpha()`**: Returns `True` if all characters in the string are alphabetic (a-z, A-Z).
- **`s.isdigit()`**: Returns `True` if all characters are digits (0-9).
- **`s.isalnum()`**: Returns `True` if all characters are alphanumeric (letters or digits).
- **`s.isspace()`**: Returns `True` if string contains only whitespace characters (spaces, tabs, newlines).
- **`s.islower()`**: Returns `True` if all cased characters are lowercase.
- **`s.isupper()`**: Returns `True` if all cased characters are uppercase.
- **`s.istitle()`**: Returns `True` if string is in title case.
- **`s.isnumeric()`**: Returns `True` if all characters are numeric (includes digits, Unicode fractions, Roman numerals).

#### D. Trimming, Splitting & Joining Methods
- **`s.strip([chars])`**: Removes leading and trailing whitespace (or specified characters).
- **`s.lstrip([chars])`**: Removes leading (left) whitespace or characters.
- **`s.rstrip([chars])`**: Removes trailing (right) whitespace or characters.
- **`s.split(sep=None, maxsplit=-1)`**: Splits string into a **list of strings** using specified separator `sep` (default is whitespace).
- **`s.rsplit(sep)`**: Splits string starting from the right.
- **`s.splitlines()`**: Splits string at line breaks (`\n`, `\r\n`) and returns a list of lines.
- **`delimiter.join(iterable)`**: Joins elements of an iterable (list/tuple of strings) into a single string using `delimiter`.  
  - *Example:* `"-".join(["a", "b", "c"]) -> "a-b-c"`
- **`s.replace(old, new[, count])`**: Replaces occurrences of `old` substring with `new` substring.
- **`s.partition(sep)`**: Splits string at the first occurrence of `sep` and returns a 3-tuple: `(head, sep, tail)`.
- **`s.zfill(width)`**: Pads string on the left with zero (`0`) digits until it reaches specified `width`.

---

## 5. Functions, Scope (LEGB), Arguments & Recursion

### Q15. Explain the LEGB Rule for variable scope resolution.
**Answer:**
When looking up a variable name, Python searches four scopes in strict order:
1. **L (Local):** Names defined inside the currently executing function.
2. **E (Enclosing):** Names in enclosing/outer functions (relevant in nested functions and closures).
3. **G (Global):** Names defined at the top level of the module file.
4. **B (Built-in):** Pre-defined module names in Python (e.g., `len`, `range`, `print`).

---

### Q16. What is the difference between `*args` and `**kwargs`?
**Answer:**
- **`*args` (Non-Keyword / Positional Arguments):** Passes a variable number of positional arguments to a function as a **tuple**.
- **`**kwargs` (Keyword Arguments):** Passes a variable number of keyword/named arguments to a function as a **dictionary**.
**Order of parameters in function definition:**
`def func(positional, *args, **kwargs)`

---

### Q17. What is Recursion? What are the essential components of a recursive function?
**Answer:**
Recursion is a programming technique where a function calls itself to solve a smaller instance of the same problem.
Essential components:
1. **Base Case:** A stopping condition that returns a value without making further recursive calls (prevents infinite recursion).
2. **Recursive Case:** The logic where the function calls itself with modified (usually reduced) inputs.
*Without a base case, recursion raises a `RecursionError` (Stack Overflow).*

---

### Q18. What is a Lambda Function?
**Answer:**
A `lambda` function is an anonymous, inline function that contains a single expression.
**Syntax:** `lambda arguments: expression`
- It implicitly returns the result of the expression.
- Best used for short, temporary operations (e.g., passing as key functions in `sort()`, `map()`, or `filter()`).

---

## 6. Collections: Lists, Tuples, Sets, Dictionaries & Comprehensions

### Q19. Compare List, Tuple, Set, and Dictionary.
**Answer:**

| Property | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{"a": 1}` |
| **Ordered** | Yes | Yes | No | Yes (Python 3.7+) |
| **Mutable** | Yes | No | Yes | Yes |
| **Duplicates** | Allowed | Allowed | Not Allowed | Keys: Unique, Values: Duplicates |
| **Indexing** | Yes | Yes | No | By Key |

---

### Complete List Methods Reference
- **`lst.append(x)`**: Adds element `x` to the end of the list.
- **`lst.extend(iterable)`**: Appends all items from an `iterable` (list, tuple, set) to the end of the list.
- **`lst.insert(i, x)`**: Inserts element `x` at specified index `i`.
- **`lst.remove(x)`**: Removes the **first occurrence** of element `x`. Raises `ValueError` if `x` is not present.
- **`lst.pop([i])`**: Removes and returns element at index `i` (default is last element `-1`). Raises `IndexError` if list is empty.
- **`lst.clear()`**: Removes all elements from the list, making it empty `[]`.
- **`lst.index(x[, start[, end]])`**: Returns zero-based index of the first occurrence of `x`.
- **`lst.count(x)`**: Returns total number of times `x` appears in the list.
- **`lst.sort(key=None, reverse=False)`**: Sorts items of the list **in-place**.
- **`lst.reverse()`**: Reverses elements of the list **in-place**.
- **`lst.copy()`**: Returns a shallow copy of the list.

---

### Complete Tuple Methods Reference
- **`tup.count(x)`**: Returns total occurrences of `x` in tuple.
- **`tup.index(x)`**: Returns index of first occurrence of `x`. Raises `ValueError` if not found.

---

### Complete Dictionary Methods Reference
- **`d.get(key[, default])`**: Returns value for `key` if present; else returns `default` (or `None`). **Does not raise KeyError**.
- **`d.keys()`**: Returns a view object displaying all dictionary keys.
- **`d.values()`**: Returns a view object displaying all dictionary values.
- **`d.items()`**: Returns a view object displaying key-value pairs as `(key, value)` tuples.
- **`d.update([other])`**: Updates dictionary with key-value pairs from another dictionary or iterable.
- **`d.pop(key[, default])`**: Removes specified `key` and returns its value. Returns `default` if key is not found.
- **`d.popitem()`**: Removes and returns the last inserted `(key, value)` pair as a tuple (FIFO/LIFO order in Python 3.7+).
- **`d.setdefault(key[, default])`**: Returns value of `key`. If `key` is not present, inserts `key` with specified `default` value.
- **`d.fromkeys(iterable[, value])`**: Class method that creates a new dictionary with keys from `iterable` and values set to `value`.
- **`d.clear()`**: Empties the dictionary.
- **`d.copy()`**: Returns a shallow copy of the dictionary.

---

### Complete Set Methods Reference
- **`s.add(x)`**: Adds element `x` to the set.
- **`s.update(iterable)`**: Adds elements from `iterable` to the set.
- **`s.remove(x)`**: Removes element `x` from set. **Raises KeyError** if `x` is not found.
- **`s.discard(x)`**: Removes element `x` from set if present. **Does NOT raise KeyError** if `x` is absent.
- **`s.pop()`**: Removes and returns an arbitrary element from the set. Raises `KeyError` if set is empty.
- **`s.clear()`**: Removes all elements from the set.
- **`s1.union(s2)` (`s1 | s2`)**: Returns a new set containing all unique elements from both sets.
- **`s1.intersection(s2)` (`s1 & s2`)**: Returns a new set with elements common to both sets.
- **`s1.difference(s2)` (`s1 - s2`)**: Returns a new set with elements in `s1` but not in `s2`.
- **`s1.symmetric_difference(s2)` (`s1 ^ s2`)**: Returns a new set with elements in either set, but not in both.
- **`s1.issubset(s2)`**: Returns `True` if `s1` is a subset of `s2`.
- **`s1.issuperset(s2)`**: Returns `True` if `s1` contains all elements of `s2`.
- **`s1.isdisjoint(s2)`**: Returns `True` if `s1` and `s2` have no common elements.

---

### Q20. Why are Dictionary lookups $O(1)$ constant time complexity?
**Answer:**
Python dictionaries are implemented using **Hash Tables**. When accessing `dict[key]`, Python computes the hash value `hash(key)` to instantly locate the exact memory address slot where the corresponding value is stored, enabling $O(1)$ average time complexity.

---

### Q21. Compare List Comprehension vs. Map & Filter.
**Answer:**
- **List Comprehension:** Provides a concise syntax to construct lists.
  - Example: `[x**2 for x in nums if x % 2 == 0]`
- **`map()` & `filter()`:** Functional built-ins that return lazy iterators.
  - List comprehension is generally considered more Pythonic and readable than chaining `map()` and `filter()`.

---

## 7. Useful Built-in Functions Reference

- **`len(s)`**: Returns the total number of items in a sequence or collection.
- **`sum(iterable[, start])`**: Sums `start` and items of an iterable from left to right.
- **`max(iterable, key=None)`**: Returns the largest item in an iterable or among two/more arguments.
- **`min(iterable, key=None)`**: Returns the smallest item in an iterable.
- **`sorted(iterable, key=None, reverse=False)`**: Returns a **new** sorted list from the items in iterable.
- **`reversed(seq)`**: Returns a reverse iterator over sequence.
- **`enumerate(iterable, start=0)`**: Returns an enumerate object generating tuples of `(index, item)`.
- **`zip(*iterables)`**: Aggregates elements from each of the iterables into tuples.
- **`map(function, iterable)`**: Applies `function` to every item of `iterable` and returns an iterator.
- **`filter(function, iterable)`**: Filters items from `iterable` for which `function(item)` returns `True`.
- **`all(iterable)`**: Returns `True` if **all** elements in iterable are Truthy (or if iterable is empty).
- **`any(iterable)`**: Returns `True` if **at least one** element in iterable is Truthy.
- **`abs(x)`**: Returns the absolute value of a number `x`.
- **`round(number[, ndigits])`**: Rounds a number to `ndigits` precision after the decimal point.
- **`ord(ch)`**: Returns the integer ASCII / Unicode code point of a single character `ch`.
- **`chr(i)`**: Returns the character string corresponding to integer Unicode code point `i`.
- **`type(object)`**: Returns the data type class of `object`.
- **`id(object)`**: Returns the unique integer memory identity address of `object`.
- **`isinstance(object, classinfo)`**: Returns `True` if `object` is an instance of `classinfo`.

---

## 8. Math Module Methods Reference (`import math`)

- **`math.sqrt(x)`**: Returns the square root of `x`.
- **`math.pow(x, y)`**: Returns `x` raised to power `y` (always returns float).
- **`math.ceil(x)`**: Rounds `x` **up** to the nearest integer.
- **`math.floor(x)`**: Rounds `x` **down** to the nearest integer.
- **`math.factorial(x)`**: Returns the factorial of integer `x`.
- **`math.gcd(a, b)`**: Returns the greatest common divisor of integers `a` and `b`.
- **`math.isclose(a, b)`**: Checks whether values `a` and `b` are close to each other.
- **`math.pi`**: Mathematical constant $\pi = 3.14159...$
- **`math.e`**: Mathematical constant $e = 2.71828...$

---

## 9. Algorithms & Special Number Concepts

### Q22. What is an Armstrong Number?
**Answer:**
An Armstrong number (narcissistic number) is an $n$-digit number equal to the sum of its digits each raised to the $n$-th power.
- *Example:* $153$ ($3$ digits) $\rightarrow 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$.

---

### Q23. What is a Perfect Number?
**Answer:**
A Perfect Number is a positive integer equal to the sum of all its proper divisors (excluding the number itself).
- *Example:* $6 \rightarrow 1 + 2 + 3 = 6$.
- *Example:* $28 \rightarrow 1 + 2 + 4 + 7 + 14 = 28$.

---

### Q24. Differentiate Linear Search vs. Binary Search.
**Answer:**
- **Linear Search:** Sequentially checks each element. Works on unsorted arrays. Time complexity: $O(N)$.
- **Binary Search:** Repeatedly divides a sorted search range in half. **Requires sorted input**. Time complexity: $O(\log N)$.

---

## 10. Advanced Python Interview Concepts

### Q25. Explain Shallow Copy vs. Deep Copy.
**Answer:**
- **Shallow Copy (`copy.copy()`):** Constructs a new container object, but populates it with **references** to the child objects contained in the original. Modifying nested mutable objects affects both original and copied structures.
- **Deep Copy (`copy.deepcopy()`):** Recursively constructs a new container object and duplicates **all nested objects**, creating a completely independent object graph in memory.

---

### Q26. How does Memory Management and Garbage Collection work in Python?
**Answer:**
1. **Reference Counting:** Python maintains a counter of references pointing to each object. When reference count drops to `0`, the object memory is deallocated immediately.
2. **Generational Garbage Collector (GC):** Handles cyclic references (e.g., Object A referencing Object B while Object B referencing Object A). GC classifies objects into 3 generations (Gen 0, Gen 1, Gen 2) based on object age and collects cyclic dead references periodically.

---

### Q27. What is the GIL (Global Interpreter Lock)?
**Answer:**
The GIL is a mutex (lock) in CPython that prevents multiple native threads from executing Python bytecodes simultaneously on multiple CPU cores.
- **Impact:** Python multithreading is effective for **I/O-bound** tasks, but does not provide multi-core parallel speedups for **CPU-bound** tasks (multiprocessing should be used instead for CPU-bound tasks).

---

### Q28. What is Duck Typing in Python?
**Answer:**
Duck Typing is a core dynamic typing concept summarized by: *"If it walks like a duck and quacks like a duck, it's a duck."*
Python cares about whether an object has specific methods/attributes at runtime rather than its explicit class hierarchy.

---

### Q29. What is `__name__ == "__main__"`?
**Answer:**
`__name__` is a special built-in variable set by Python:
- If a script is executed directly, `__name__` is assigned `"__main__"`.
- If a script is imported as a module into another file, `__name__` is set to the module's filename.
This check allows code to run when executed as a script, but prevents execution when imported as a library.
