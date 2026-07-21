#Find the sum of even digits in a number.Sample Input: N = 864521

n = 864521
sum = 0
for i in str(n):
    if int(i) %2 == 0:
        sum += int(i)
print(sum)