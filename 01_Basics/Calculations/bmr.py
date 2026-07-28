# Question: Write a Python program to calculate Basal Metabolic Rate (BMR) from age, weight, and height.

age = int(input("Enter the age:"))
weight = float(input("Enter the weight in kg:"))
height = float(input("Enter the height in cm:"))

height = height / 100
bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

print(bmr)
