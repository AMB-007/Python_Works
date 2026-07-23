# ============================================================
#  TOPIC: Decision Making — if / elif / else
# ============================================================

# DEFINITION:
#   Decision making lets the program choose which block of
#   code to run based on whether a condition is True or False.

# ── IF / ELIF / ELSE ─────────────────────────────────────
# SYNTAX:
#   if condition:
#       # runs when condition is True
#   elif another_condition:
#       # runs when first is False, this is True
#   else:
#       # runs when ALL above conditions are False

# EXAMPLE 1 – Simple if/else:
age = int(input("Enter age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# EXAMPLE 2 – if / elif / else (multiple conditions):
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

# ── NESTED IF ─────────────────────────────────────────────
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

# ── TERNARY OPERATOR ──────────────────────────────────────
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

# ── LOGICAL OPERATORS IN CONDITIONS ──────────────────────
#   and → both must be True
#   or  → at least one must be True
#   not → flips True to False

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
#   → Indentation (4 spaces) defines the block — it is MANDATORY
#   → elif is "else if" — checked only if previous conditions failed
#   → else is optional, catches everything not matched above
#   → Ternary is great for simple assignments, avoid nesting it
