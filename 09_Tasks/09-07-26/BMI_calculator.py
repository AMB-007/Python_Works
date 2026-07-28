# Question: Write a Python program to calculate Body Mass Index (BMI) from weight (kg) and height (cm).

def bmi(weight, height):
    result = weight / (height ** 2)
    print(round(result, 2))

bmi(70, 1.75)
