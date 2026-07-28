# Question: Write a Python program for exception handling intro.

# Introduction to Exception Handling in Python
# Try block holds risky code; Except block handles runtime exceptions gracefully.

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

try:
    result = num_1 / num_2
    print("Division Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not possible.")

print("Program execution completed successfully.")

