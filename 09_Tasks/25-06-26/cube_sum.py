# Question: Write a Python program for cube sum.

n = int(input("Enter the number:"))
i = 1
sum = 0
while( i<= n):
    sum += i*i*i
    i += 1
print(sum)
