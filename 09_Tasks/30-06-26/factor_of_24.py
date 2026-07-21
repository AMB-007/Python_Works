# Print all factors of a given number.Sample Input: N = 24

n = 24
for i in range(1,n+1):
    if n % i == 0:
        print(i)