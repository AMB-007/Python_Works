# find the largest element with maximum frequency


numbers = [2, 4, 2, 5, 6, 2, 4]
max_frequency = 0
element = 0
for i in numbers:
    frequency = numbers.count(i)
    if frequency > max_frequency:
        max_frequency = frequency
        element = i
print(element,max_frequency)
