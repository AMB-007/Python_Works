#1. Find Armstrong Numbers in a List
# Given a list of numbers, print all Armstrong numbers.
# Sample Input: [153,123,370,456,407,500


numbers = [153, 123, 370, 456, 407, 500]

armstrong = []

for num in numbers:
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

    if total == num:
        armstrong.append(num)

print(armstrong)