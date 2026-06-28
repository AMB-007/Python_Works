# wap to get the total number of digits in a number.

n = int(input("Enter the number :"))
if n == 0:
    print(f"count is 1")
else:
    count = 0
    while n != 0:
        
        count += 1
        n = n // 10
    print(count)



