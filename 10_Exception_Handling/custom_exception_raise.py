# Question: Write a Python program for custom exception raise.

# Raising custom exceptions manually using the 'raise' keyword

age = int(input("Enter your age: "))

if age < 18:
    raise Exception("Invalid age: Must be 18 or older to proceed.")

print("Access granted! Thank you.")

