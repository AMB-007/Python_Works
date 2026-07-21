n = int(input("Enter the number :"))

i = 1
count = 1
while( i <= n):
    if i % 2 == 0 and i % 7 == 0:
        count += i
    i += 1
print(count)