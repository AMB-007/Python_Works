# Question: Write a Python program for io and variables.

# ============================================================
#  TOPIC: IO (Input / Output) and Variables
# ============================================================

# DEFINITION:
#   Variables store data in memory with a name.
#   Input reads data from the user via keyboard.
#   Output prints data to the screen.

# â”€â”€ VARIABLES â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# SYNTAX:  variable_name = value

name = "Arjun"          # str  (string)
age  = 21               # int  (integer)
gpa  = 8.5              # float
is_student = True       # bool (True / False)

# Rules for variable names:
#   âœ” Start with a letter or underscore: name, _count
#   âœ” Can have letters, digits, underscores: total_marks2
#   âœ˜ Cannot start with a digit: 2name â† WRONG
#   âœ˜ Cannot use keywords: if, for, while â† WRONG

# Multiple assignment:
x = y = z = 0           # all three get 0
a, b, c = 10, 20, 30    # each gets its own value

# â”€â”€ INPUT â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# SYNTAX:  variable = input("prompt message")
# NOTE:    input() ALWAYS returns a STRING

name  = input("Enter your name: ")      # string
age   = int(input("Enter your age: "))  # converted to int
price = float(input("Enter price: "))   # converted to float

# â”€â”€ OUTPUT â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# SYNTAX:  print(value)

print("Hello, World!")              # plain string
print("Name:", name)                # comma separates with space
print("Age =", age)

# f-string (recommended â€“ clean and readable):
print(f"My name is {name} and I am {age} years old.")

# format():
print("Name: {} | Age: {}".format(name, age))

# print() options:
print("A", "B", "C", sep="-")      # A-B-C  (custom separator)
print("Hello", end=" ")            # stays on same line
print("World")                     # Hello World

# â”€â”€ DATA TYPES â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#   type(x) â†’ shows the data type
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>

# KEY POINTS:
#   â†’ Use int() / float() to convert input for calculations
#   â†’ f-strings are the cleanest way to format output
#   â†’ Variables are case-sensitive: Name â‰  name

