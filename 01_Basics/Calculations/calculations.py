# Question: Write a Python program for calculations.

# ============================================================
#  TOPIC: Calculations in Python
# ============================================================

# DEFINITION:
#   Calculations involve using arithmetic operators to perform
#   mathematical operations on numbers (integers & floats).

# OPERATORS:
#   +   â†’ Addition          : 5 + 3  = 8
#   -   â†’ Subtraction       : 5 - 3  = 2
#   *   â†’ Multiplication    : 5 * 3  = 15
#   /   â†’ Division (float)  : 5 / 2  = 2.5
#   //  â†’ Floor Division    : 5 // 2 = 2
#   %   â†’ Modulus (remainder): 5 % 2 = 1
#   **  â†’ Exponentiation    : 2 ** 3 = 8

# SYNTAX:
#   result = operand1  operator  operand2

# EXAMPLES:
price = 100
tax = 18
total = price + (price * tax / 100)
print("Total after tax:", total)       # 118.0

# Average of 5 subjects
marks = [80, 90, 75, 85, 95]
average = sum(marks) / len(marks)
print("Average:", average)             # 85.0

# Simple Interest: SI = (P * R * T) / 100
p, r, t = 1000, 5, 2
si = (p * r * t) / 100
print("Simple Interest:", si)          # 100.0

# Area and Perimeter of Rectangle
length, breadth = 10, 5
area = length * breadth                # 50
perimeter = 2 * (length + breadth)    # 30

# BMI: weight(kg) / height(m)^2
weight, height = 70, 1.75
bmi = weight / (height ** 2)
print("BMI:", round(bmi, 2))           # 22.86

# KEY POINTS:
#   â†’ Always convert input to int() or float() before calculations
#   â†’ Use round(value, 2) to limit decimal places
#   â†’ // gives integer result, / always gives float

