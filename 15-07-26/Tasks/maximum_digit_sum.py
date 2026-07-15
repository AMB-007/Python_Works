# Find Number with Maximum Digit Sum
# Sample Input: [123,999,456,87]

numbers = [123,999,456,87]
max_sum = 0
max_num = 0

for num in numbers:
    temp = num
    digit_sum = 0

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp = temp // 10

    if digit_sum > max_sum:
        max_sum = digit_sum
        max_num = num

print(max_num)
print(max_sum)