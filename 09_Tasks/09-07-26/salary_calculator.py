# Question: Write a Python program for salary calculator.

def salary(basic):
    total = basic + (basic * 30 / 100)
    print(int(total))

salary(20000)
