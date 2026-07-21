def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


"""


RECURSIVE FUNCTION
its a techinique where a function calls itself to solve the same problem
==================
WORKING
when we call  the factorial(5) it didnt get the immediate answers
it has to wind up a stack of function calls until it hits the base case
==================


return 5 * factorial(4) waiting
return 4 * factorial(3) waiting
return 3 * factorial(2) waiting
return 2 * factorial(1) waiting










"""