# check and print the armstrong numbers in a range from 1 to 1000






n = int(input("Enter N :"))

for i in range(1,n):
    sum = 0
    temp = i
    length = len(str(i))
    for j in str(i):
        
        sum += int(j) ** length
        
    if temp == sum:
        print(temp)
    

    




