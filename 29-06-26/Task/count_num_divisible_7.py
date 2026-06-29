# Count numbers divisible by 7 from 1 to N.Sample Input: N = 100
n = int(input("Enter N :"))
count = 0
for i in range(1,n+1):
    if i %7 == 0:
        count += 1
print(count)

