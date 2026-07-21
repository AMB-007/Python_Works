# Find the smallest digit in a number.Sample Input: N = 583926

n = 583926
smallest = 9
for i in str(n):
   
    if int(i) < smallest:
        smallest = int(i)
print(smallest)