# Question: Write a Python program for count multiple of 4.

n = int(input("Enter the number :"))
i = 1
count = 0
while( i <= n):
    if i % 4 == 0:
        count += 1
    i += 1
print(count)
