# wap to get the missing numbers from the sequence of the numbers form the list
numbers = [3,2,9,4,8,1,6]

for i in range(min(numbers),max(numbers) + 1):
    if i not in numbers:
        print(i)