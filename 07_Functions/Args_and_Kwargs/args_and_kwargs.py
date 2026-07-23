# ============================================================
#  TOPIC: Functions — *args and **kwargs
# ============================================================

# DEFINITION:
#   *args allows a function to accept ANY NUMBER of positional
#   arguments. They are received as a TUPLE inside the function.
#
#   **kwargs allows a function to accept ANY NUMBER of keyword
#   arguments. They are received as a DICTIONARY inside the function.

# ── *args (Variable Positional Arguments) ────────────────
# SYNTAX:  def func(*args):
#   The * before the name collects all extra positional args into a tuple.

def add_all(*args):
    print(args)             # tuple of all arguments
    return sum(args)

print(add_all(1, 2, 3))         # 6
print(add_all(10, 20, 30, 40))  # 100
print(add_all(5))               # 5

# Using *args in a loop:
def print_all(*args):
    for item in args:
        print(item)

print_all("apple", "banana", "cherry")

# Mixing normal parameters with *args:
# Normal params MUST come before *args
def greet(msg, *names):
    for name in names:
        print(f"{msg}, {name}!")

greet("Hello", "Arjun", "Ravi", "Priya")
# Hello, Arjun!
# Hello, Ravi!
# Hello, Priya!

# ── **kwargs (Variable Keyword Arguments) ────────────────
# SYNTAX:  def func(**kwargs):
#   The ** collects all keyword arguments into a dictionary.

def show_info(**kwargs):
    print(kwargs)       # {'name': 'Arjun', 'age': 21}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Arjun", age=21, city="Chennai")

# ── Combining both ────────────────────────────────────────
# ORDER: normal params → *args → **kwargs

def full_example(required, *args, **kwargs):
    print("Required:", required)
    print("Extra args:", args)
    print("Keyword args:", kwargs)

full_example("must", 1, 2, 3, name="Arjun", age=21)
# Required: must
# Extra args: (1, 2, 3)
# Keyword args: {'name': 'Arjun', 'age': 21}

# ── Unpacking with * and ** ───────────────────────────────
# You can also UNPACK a list/tuple into positional args:
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))       # 6  (unpacks list into a, b, c)

# Unpack a dictionary into keyword arguments:
info = {"a": 10, "b": 20, "c": 30}
print(add(**info))      # 60

# KEY POINTS:
#   → *args  → tuple  → access like args[0], or loop with for
#   → **kwargs → dict → access like kwargs["key"] or .items()
#   → Order in definition: (normal, *args, **kwargs)
#   → * and ** can also UNPACK when calling a function
#   → You can name them anything: *numbers, **options — * and ** matter
