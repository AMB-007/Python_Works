# Question: Write a Python program using while loop to prompt input until user enters a number greater than 5.

number = int(input("Enter the number :"))
while number <= 5:
    number = int(input("Enter the number :"))
print(f"the last number is {number}")
