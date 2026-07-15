# wap to get the second largest number forn the list

numbers = [4, 11, 5]

largest = numbers[0]
second_largest = numbers[1]
for i in numbers:
    if i > largest and i > second_largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i < largest:
        second_largest = i
print(largest,second_largest)
