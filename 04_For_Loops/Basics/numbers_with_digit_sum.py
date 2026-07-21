
n = int(input("Enter a number"))
for i in range(1,n+1):
    sum = 0
    for j in str(i):
        sum += int(j)
    if sum %2 == 0 and i %3 == 0 and i %5 != 0:
        print("Golden number")
        print(i)



