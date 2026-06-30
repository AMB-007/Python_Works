# Find the largest digit in a number.Sample Input: N = 583926
n = 583926
largest = 0
for i in str(n):
    digit = int(i)
    if digit > largest:
        largest = digit
print(largest)