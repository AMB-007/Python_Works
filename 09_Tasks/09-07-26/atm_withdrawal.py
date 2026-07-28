# Question: Write a Python program for atm withdrawal.

def withdraw(balance, amount):
    remaining = balance - amount
    print(remaining)

withdraw(5000, 1200)
