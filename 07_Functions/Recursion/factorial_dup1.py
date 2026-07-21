# definr=e a function to return the factorial


def factorial(num_1):
    fact = 1
    for i in range(1,num_1+1):
        fact *= i
    return fact
print(factorial(5))



"""
retutn statement
the return statement is used inside a function to send a value back to the place
Where the function was called
once return is executed the function stops running
"""
