# Question: Write a Python program for filter intro.

#filter()
"""
keeps nly items for which the condition is true
Syntax
======
filter(function,iterable)

"""

number = [1,2,3,4,5,6,7,8]
print(list(filter(lambda a:a%2 == 0,number)))

#get the numbers divisible by 3 from 1 to 20
print(list(filter(lambda a:a % 3 == 0,  range (1,21))))

