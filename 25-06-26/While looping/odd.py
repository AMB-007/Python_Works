# wap to get the numbers should be odd and divisible by 3
# from 1 to n

n = int(input("Enter the number:"))
i = 1
while( i<= n):
    if( i % 2 !=0 and i % 3 == 0):
        print(i)
    i += 1