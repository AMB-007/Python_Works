# Count the number of factors of a given number.Sample Input: N = 36
n = int(input("Enter N :"))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
print(count)