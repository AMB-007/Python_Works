# Question: Write a Python program to evaluate voting and license eligibility based on age conditions.

age = int(input("Enter the age:"))

if age >= 18:
    print(f"He can vote")
elif age == 17:
    print(f"He can learn driving")
elif age == 16 :
    print(f"He can buy lottery")
else:
    print(f"He can go to Trick or treating")

