# Find the sum of even numbers from 1 to N.Sample Input: N = 20
n = int(input("Enter N :"))

sum = 0
for i in range(1,n+1):
    if i %2 == 0:
        sum += i
print(sum)
    