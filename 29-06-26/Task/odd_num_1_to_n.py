#Find the sum of odd numbers from 1 to N.Sample Input: N = 15
n = int(input("Enter N :"))
sum = 0
for i in range(1,n+1):
    if i %2 != 0:
        sum += i
print(sum)