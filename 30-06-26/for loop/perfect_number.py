n = int(input("Enter N :"))
sum = 0
for i in range(1,n//2+1):
    print(i)
    if n % i == 0:
        sum += i