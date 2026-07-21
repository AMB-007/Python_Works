# Find the largest digit in a number.Sample Input: N = 583926
n = 583926
largest = 0
for i in str(n):
    
    if int(i) > largest:
        largest = int(i)
print(largest)