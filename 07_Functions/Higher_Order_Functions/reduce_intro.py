"""
reduce()
reduce(function,iterable)




combines all items into one final value
it must be imported from functiontools

"""


from functools import reduce
numbers = [1,2,3,4,5]
print(reduce(lambda a,b:a+b,numbers))

"""
a,b with first two values
a = 1 , b = 2
previous result with next value
a = 3 , b = 3
previous result with next vslue
a = 6 , b = 4
"""