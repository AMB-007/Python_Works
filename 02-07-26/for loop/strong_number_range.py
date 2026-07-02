
for i in range(1,1000):
    sum = 0
    for j in  str(i):
            fact = 1
            for k in range(1,int(j)+1):
                fact *= int(k)
            sum += fact
    if sum == i:
        print(i)

       