# Question: Write a Python program to calculate simple interest from principal amount, rate, and tenure.


def interest(p, r, t):
    si = (p * r * t) / 100
    print(int(si))

interest(10000, 8, 2)


