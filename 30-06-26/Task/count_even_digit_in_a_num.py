# Count the even digits in a number.Sample Input: N = 98765432


n = 98765432
count = 0
for i in str(n):
    if int(i) %2 == 0:
        count += 1
print(count)