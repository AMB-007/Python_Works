# Question: Write a Python program to find the second smallest element in a list of numbers.

numbers = [20, 13, 41, 30, 7, 11]

smallest = float("inf")
sec_smallest = float("inf")

for i in numbers:
    if i < smallest:
        sec_smallest = smallest
        smallest = i
    elif i > smallest and i < sec_smallest:
        sec_smallest = i

print("List:", numbers)
print("Second Smallest element:", sec_smallest)
