# Question: Write a Python program for map intro.

#list
"""
Applies a function to every line.
syntax
=======
map(function,iterable)
 
 
 """

number = [1,2,3,4,5]
print(list(map(lambda a:a ** 2,number)))


numbers = [1,2,3,4,5] #[odd,even,odd,even]
print(list(map(lambda a:"even" if a % 2 == 0 else "odd",numbers)))
