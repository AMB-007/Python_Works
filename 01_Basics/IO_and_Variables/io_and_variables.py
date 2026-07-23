# ============================================================
#  TOPIC: IO (Input / Output) and Variables
# ============================================================

# DEFINITION:
#   Variables store data in memory with a name.
#   Input reads data from the user via keyboard.
#   Output prints data to the screen.

# ── VARIABLES ────────────────────────────────────────────
# SYNTAX:  variable_name = value

name = "Arjun"          # str  (string)
age  = 21               # int  (integer)
gpa  = 8.5              # float
is_student = True       # bool (True / False)

# Rules for variable names:
#   ✔ Start with a letter or underscore: name, _count
#   ✔ Can have letters, digits, underscores: total_marks2
#   ✘ Cannot start with a digit: 2name ← WRONG
#   ✘ Cannot use keywords: if, for, while ← WRONG

# Multiple assignment:
x = y = z = 0           # all three get 0
a, b, c = 10, 20, 30    # each gets its own value

# ── INPUT ─────────────────────────────────────────────────
# SYNTAX:  variable = input("prompt message")
# NOTE:    input() ALWAYS returns a STRING

name  = input("Enter your name: ")      # string
age   = int(input("Enter your age: "))  # converted to int
price = float(input("Enter price: "))   # converted to float

# ── OUTPUT ───────────────────────────────────────────────
# SYNTAX:  print(value)

print("Hello, World!")              # plain string
print("Name:", name)                # comma separates with space
print("Age =", age)

# f-string (recommended – clean and readable):
print(f"My name is {name} and I am {age} years old.")

# format():
print("Name: {} | Age: {}".format(name, age))

# print() options:
print("A", "B", "C", sep="-")      # A-B-C  (custom separator)
print("Hello", end=" ")            # stays on same line
print("World")                     # Hello World

# ── DATA TYPES ───────────────────────────────────────────
#   type(x) → shows the data type
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>

# KEY POINTS:
#   → Use int() / float() to convert input for calculations
#   → f-strings are the cleanest way to format output
#   → Variables are case-sensitive: Name ≠ name
