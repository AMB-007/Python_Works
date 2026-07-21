

n = 145
sum = 0
for num in str(n):
    fact= 1
    for i in range(1,int(num)+1):
        fact *= i
    sum += fact
print("strong_number" if sum == n else "not strong")