# . Find the sum of digits of a number.Sample Input: N = 5839

n = 5839
sum = 0
for i in str(n):
    sum += int(i)
print(sum)
