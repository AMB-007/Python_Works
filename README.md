# 🐍 Python Works — Topic-Wise Master Repository & Practice Collection

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Structure](https://img.shields.io/badge/Architecture-Topic--Wise-green.svg?style=for-the-badge)](https://github.com/AMB-007/Python_Works)
[![License](https://img.shields.io/badge/License-MIT-orange.svg?style=for-the-badge)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-brightgreen.svg?style=for-the-badge)](https://github.com/AMB-007/Python_Works/commits/main)

Welcome to **Python Works**! A comprehensive, structured, and topic-organized repository containing core Python programming concepts, data structures, algorithms, problem-solving tasks, and technical interview preparation resources.

Every single program file in this repository is self-contained and begins with an explicit `# Question:` header defining the problem statement.

---

## 📌 Table of Contents
- [📖 Repository Architecture](#-repository-architecture)
- [📚 Topic Roadmap Breakdown](#-topic-roadmap-breakdown)
- [🗓️ Daily Tasks Directory (`09_Tasks`)](#️-daily-tasks-directory-09_tasks)
- [📘 Technical Interview & Theory Guide](#-technical-interview--theory-guide)
- [🚀 Getting Started & Execution](#-getting-started--execution)
- [🛠️ Features & Code Standards](#️-features--code-standards)

---

## 📖 Repository Architecture

The repository is modularized into **12 Core Topic Folders**, **Sub-Topic Directories**, **Daily Practice Task Sets**, and **Reference Documentation**:

```
Python_Works/
├── 📁 01_Basics/                  # Variables, Data Types, Operators, Conversions
│   ├── 📁 Calculations/          # Bill split, BMI, BMR, Electricity bill
│   ├── 📁 Conversions/           # Temperature, Days/Hours/Seconds conversion
│   ├── 📁 IO_and_Variables/      # Input/Output, Arithmetic, Zero shifting
│   └── 📁 Operators/             # Assignment, Relational, Swap numbers
│
├── 📁 02_Decision_Making/         # Conditional Statements & Control Flow
│   ├── 📁 If_Else/               # Age, ATM withdrawal, Leap year, Odd/Even
│   ├── 📁 Logical_Operators/     # Divisibility, Mark range validation
│   ├── 📁 Nested_If/             # Scholarship, Road tax calculation
│   └── 📁 Ternary_Operator/      # Shorthand conditional evaluation
│
├── 📁 03_While_Loops/             # Iterative Control with While Loops
│   ├── 📁 Basics/                # Input validation, Range bounds, Counters
│   ├── 📁 Number_Problems/       # Digit counting, Factors, Sum/Product
│   └── 📁 Special_Numbers/       # Armstrong, Palindrome, Harshad, Spy numbers
│
├── 📁 04_For_Loops/               # Range-based Loops & Iterations
│   ├── 📁 Basics/                # Digit sum, Selective sum, Range printing
│   ├── 📁 Number_Problems/       # Factorial, Harshad number check
│   ├── 📁 Range_Programs/        # Prime / Perfect / Strong numbers in ranges
│   └── 📁 Special_Numbers/       # Automorphic, Prime, Perfect, Spy numbers
│
├── 📁 05_Strings/                 # Text Processing & String Manipulation
│   ├── 📁 Basics/                # String slicing, Methods overview
│   ├── 📁 Case_and_Characters/   # Swapcase, Case counting, Character filtering
│   └── 📁 Frequency_and_Search/  # Character frequency, Repeating/Unique chars
│
├── 📁 06_Patterns/                # Geometric & Pattern Printing
│   ├── 📄 star_patterns.py       # Star Pyramids, Inverted Triangles
│   └── 📄 patterns.py            # Number grids, Alphabet matrices
│
├── 📁 07_Functions/               # Modular Code, Scope, & Functional Tools
│   ├── 📁 Args_and_Kwargs/       # *args and **kwargs parameter handling
│   ├── 📁 Basics/                # Function definitions, Return values
│   ├── 📁 Higher_Order_Functions/# Built-in map(), filter(), reduce()
│   ├── 📁 Lambda_Functions/      # One-line anonymous lambda functions
│   ├── 📁 Math_Functions/        # Prime, Armstrong, Perfect number functions
│   ├── 📁 Modules/               # Module imports and helper files
│   ├── 📁 Packages/              # Custom packages (e.g. calculator)
│   ├── 📁 Recursion/             # Recursive Factorial implementations
│   └── 📁 String_Functions/      # Anagram, Pangram, Substring reversal
│
├── 📁 08_Collections/             # Data Structures & Sequence Types
│   ├── 📁 Dictionaries/          # Dict methods, Key-value lookups, Nested dicts
│   ├── 📁 List_Comprehension/    # One-line list & dict comprehensions
│   ├── 📁 List_Operations/       # Append, Insert, Remove, Rotate, Interleave
│   └── 📁 Searching_and_Sorting/ # Linear search, Largest/Smallest, Missing num
│
├── 📁 09_Tasks/                   # Date-Wise Practice & Assignment Sets
│   ├── 📁 20-06-26/              ├── 📁 06-07-26/              ├── 📁 16-07-26/
│   ├── 📁 22-06-26/              ├── 📁 09-07-26/              ├── 📁 17-07-26/
│   ├── 📁 23-06-26/              ├── 📁 10-07-26/              └── 📁 28-07-26/
│   ├── 📁 24-06-26/              ├── 📁 15-07-26/
│   └── ...                       └── ...
│
├── 📁 10_Exception_Handling/      # Error Handling & Validation
│   ├── 📄 exception_handling_intro.py  # Try-Except-Finally fundamentals
│   ├── 📄 multiple_exceptions_handling.py # Catching multiple error types
│   ├── 📄 list_index_error_handling.py # Handling IndexError
│   ├── 📄 dict_key_error_handling.py  # Handling KeyError
│   ├── 📄 custom_exception_raise.py    # Manual exception raising (`raise`)
│   └── 📄 assert_error_handling.py     # Assert statements & `AssertionError`
│
├── 📁 11_File_Handling/           # Persistent Storage & File I/O
│   ├── 📄 file_read_exception.py       # Safe reading with FileNotFoundError
│   ├── 📄 file_write_mode.py           # Writing files ("w" mode)
│   ├── 📄 file_append_mode.py          # Appending data ("a" mode)
│   ├── 📄 file_with_statement.py       # Context managers (`with open()`)
│   └── 📄 file_read_methods.py         # `readline()`, `readlines()`, `readable()`
│
├── 📁 12_OOPs/                    # Object-Oriented Programming (OOP)
│   ├── 📁 Abstraction/           # Abstract Base Classes (ABC) & @abstractmethod
│   ├── 📁 Basics/                # Classes, Objects, Instance state & ATM simulation
│   ├── 📁 Inheritance/           # Single-Level & Multi-Level Inheritance
│   └── 📁 Polymorphism/          # Polymorphism, Method Overriding & Overloading
│
├── 📁 Python-pratice/             # Practice workspace & problem sets
├── 📄 PYTHON_TECHNICAL_THEORY.md  # Comprehensive Python Interview & Theory Guide
└── 📄 README.md                   # Repository Documentation
```

---

## 📚 Topic Roadmap Breakdown

| Topic Directory | Core Concepts Covered | Key File Highlights |
|---|---|---|
| **`01_Basics`** | Arithmetic operators, user input, temperature/time unit conversions, BMI/BMR formulas. | `bmi.py`, `conversion.py`, `split_bill.py` |
| **`02_Decision_Making`** | `if-elif-else`, logical operators (`and`, `or`, `not`), ternary expressions. | `atm_machine.py`, `leap_year.py`, `scolarship.py` |
| **`03_While_Loops`** | `while` condition loops, input range validation, number digit extraction. | `guess_number_game.py`, `sum_num.py` |
| **`04_For_Loops`** | `for in range()`, range prime generation, automorphic & strong numbers. | `prime_from_1000to100.py`, `nearest_prime.py` |
| **`05_Strings`** | Slicing `[start:stop:step]`, string methods, case swapping, character frequency. | `string_slicing.py`, `manual_swapcase.py` |
| **`06_Patterns`** | Nested loops, star pyramids, right triangles, number grid matrices. | `star_patterns.py`, `patterns.py` |
| **`07_Functions`** | Functions, recursion, `*args`/`**kwargs`, `map()`, `filter()`, `reduce()`, lambda expressions. | `map_intro.py`, `filter_intro.py`, `kwargs_example.py` |
| **`08_Collections`** | Lists, Tuples, Dictionaries, Sets, List Comprehensions, element search/sort. | `nested_dict_operations.py`, `rotate_list_right.py` |
| **`10_Exception_Handling`**| `try-except-else-finally`, raising custom exceptions, `assert` debugging. | `exception_handling_intro.py`, `custom_exception_raise.py` |
| **`11_File_Handling`** | File modes (`"r"`, `"w"`, `"a"`), `with open()`, line reading methods. | `file_with_statement.py`, `file_read_methods.py` |
| **`12_OOPs`** | Classes, Objects, Inheritance, Polymorphism, Abstraction, Method Overriding/Overloading. | `abstraction_intro.py`, `atm_class_simulation.py`, `single_and_multilevel_inheritance.py` |

---

## 🗓️ Daily Tasks Directory (`09_Tasks`)

The `09_Tasks` folder aggregates practical daily homework, problem sets, and assessment tasks grouped by date:

- **`09_Tasks/17-07-26/`**: 20 Weekend Practice Tasks covering Primes, Factorials, Palindromes, String manipulations, List merging, and Second Largest without `sort()`.
- **`09_Tasks/28-07-26/`**: Advanced list rotation and array element transformation logic.

---

## 📘 Technical Interview & Theory Guide

For complete technical notes, theoretical explanations, method references, and interview Q&As, refer to:
📄 **[`PYTHON_TECHNICAL_THEORY.md`](PYTHON_TECHNICAL_THEORY.md)**

### Key Topics in Theory Guide:
1. **Core Data Types & Memory Management** (Mutable vs. Immutable, Garbage Collection, Reference Counting).
2. **Built-in Data Structure References** (Complete method list for `list`, `dict`, `set`, `str`).
3. **Built-in Functions & Math Module Reference** (`enumerate`, `zip`, `map`, `filter`, `math.sqrt`, `math.gcd`).
4. **OOP Principles** (Encapsulation, Single/Multilevel Inheritance, Polymorphism, Abstraction with `abc.ABC`).
5. **Special Number Definitions** (Armstrong, Harshad, Automorphic, Perfect, Spy numbers).

---

## 🚀 Getting Started & Execution

### Prerequisites
- Installed [Python 3.10+](https://www.python.org/downloads/)
- Git installed on your local machine

### 1. Clone the Repository
```bash
git clone https://github.com/AMB-007/Python_Works.git
cd Python_Works
```

### 2. Running a Specific Python Program
You can run any `.py` file directly using Python:

```bash
# Example 1: Run an OOP Abstraction program
python 12_OOPs/Abstraction/abstraction_intro.py

# Example 2: Run a string frequency program
python 05_Strings/Frequency_and_Search/first_repeating_char.py

# Example 3: Run a higher-order function script
python 07_Functions/Higher_Order_Functions/map_intro.py
```

### 3. Running Custom Packages
To run custom package scripts (e.g. `07_Functions/Packages`):

```bash
cd 07_Functions/Packages
python package_import_demo.py
```

---

## 🛠️ Features & Code Standards

- **Explicit Problem Statements**: Every script starts with a standardized comment:
  ```python
  # Question: Write a Python program to calculate the average marks of 5 subjects.
  ```
- **Self-Contained Executable Scripts**: Programs can be executed individually without external dependencies.
- **Clean Git Workflow**: Structured git history with zero temporary cache build artifacts (`.gitignore` enabled for `__pycache__`).

---

⭐ **Enjoy Coding!** If you find this repository helpful, consider starring the repo! 🚀
