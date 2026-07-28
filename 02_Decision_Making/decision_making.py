# Question: Write a Python program for decision making.

# ============================================================
#  TOPIC: Decision Making â€” if / elif / else
# ============================================================

# DEFINITION:
#   Decision making lets the program choose which block of
#   code to run based on whether a condition is True or False.

# â”€â”€ IF / ELIF / ELSE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# SYNTAX:
#   if condition:
#       # runs when condition is True
#   elif another_condition:
#       # runs when first is False, this is True
#   else:
#       # runs when ALL above conditions are False

# EXAMPLE 1 â€“ Simple if/else:
age = int(input("Enter age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# EXAMPLE 2 â€“ if / elif / else (multiple conditions):
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

# â”€â”€ NESTED IF â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# DEFINITION: An if statement inside another if statement.
# Used when a condition depends on another condition.

num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Negative or Zero")

# â”€â”€ TERNARY OPERATOR â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# DEFINITION: A single-line shorthand for simple if/else.
# SYNTAX:  value_if_true  if  condition  else  value_if_false

x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)   # Even

# More examples:
a, b = 5, 9
greater = a if a > b else b        # max of two
print("Greater:", greater)         # 9

status = "Adult" if age >= 18 else "Minor"

# â”€â”€ LOGICAL OPERATORS IN CONDITIONS â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#   and â†’ both must be True
#   or  â†’ at least one must be True
#   not â†’ flips True to False

salary = 50000
experience = 3
if salary > 30000 and experience >= 2:
    print("Eligible for loan")

username = "admin"
if username == "admin" or username == "superuser":
    print("Access granted")

is_banned = False
if not is_banned:
    print("User is active")

# KEY POINTS:
#   â†’ Indentation (4 spaces) defines the block â€” it is MANDATORY
#   â†’ elif is "else if" â€” checked only if previous conditions failed
#   â†’ else is optional, catches everything not matched above
#   â†’ Ternary is great for simple assignments, avoid nesting it

