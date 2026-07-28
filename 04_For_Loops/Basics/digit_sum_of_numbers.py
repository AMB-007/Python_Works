# Question: Write a Python program using for loop to calculate the sum of digits for numbers from 1 to N.

n = int(input("Enter N :"))

for i in range(1,n+1):
    sum = 0
    for j in str(i):
       
        sum += int(j)
    if sum == 10:
        print(i)



   
