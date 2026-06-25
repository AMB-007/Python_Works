# wap to get the count of number divisible by 3 from 1 to 100

i = 1
count = 0
while(i <= 100):
    if i % 3 ==0:
        count += 1
    i += 1
print(count)