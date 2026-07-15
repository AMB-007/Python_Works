# wap to remove the even numbers from the given list
numbers = [2,3,4,6,8,9,11,10]

for i in numbers.copy():
    if i %2 == 0:
        numbers.remove(i)

print(numbers)