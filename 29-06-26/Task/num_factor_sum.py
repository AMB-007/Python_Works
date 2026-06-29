# Find the sum of all factors of a given number.Sample Input: N = 36
n = int(input("Enter N :"))

sum = 0
for i in range(1,n+1):
    if n %i == 0:
        sum += i
print(sum)