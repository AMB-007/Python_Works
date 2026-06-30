n = int(input("Enter N :"))
sum = 0
for i in range(1,n):
    print(i)
    if n % i == 0:
        sum += i
print("Perfect" if sum == n  else "Not perfect")