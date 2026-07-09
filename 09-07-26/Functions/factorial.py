# definr=e a function to return the factorial


def factorial(num_1):
    fact = 1
    for i in range(1,num_1+1):
        fact *= i
    print(fact)
factorial(5)


