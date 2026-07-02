

for i in range(1000,1,-1):
    sum = 0
    for j in range(1,i//2+1):
        if i % j == 0:
            sum += j

        
    if i == sum:
        print(i)     
        