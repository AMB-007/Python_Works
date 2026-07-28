# Question: Write a Python program to check if a number is divisible by both 3 and 5 using logical AND operator.

num = int(input("Enter the number :"))

if num %5 == 0 and num %3 == 0:
    print(f"\nThe number is divisible by 5 and 3")
else:
    print(f"the number is not divisible by 5 and 3")
