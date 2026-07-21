#  Find the sum of all factors of a given number.Sample Input: N = 36

n = 36

sum = 0
for i in range(n,n+1):
    if n % i == 0:
        sum += i
print(sum)