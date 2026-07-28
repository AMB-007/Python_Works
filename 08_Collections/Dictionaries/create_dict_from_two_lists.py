# Question: Write a Python program to construct a dictionary from two lists (keys list and values list).

keys = ["name","age","place"]

values = ["arun",23,"kochi"]

elements = {}

for i in range(len(keys)):

    elements[keys[i]] = values[i]

print(elements)
