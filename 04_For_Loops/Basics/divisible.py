# Question: Write a Python program using for loop to print numbers divisible by both 3 and 5 between 10 and 100.

for i in range(10,101):

    if i % 3 == 0 and i % 5 == 0:
        print(i)
