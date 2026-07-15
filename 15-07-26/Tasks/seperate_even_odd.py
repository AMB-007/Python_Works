# Separate Even and Odd Digit Sum
# For each number calculate even digit sum and odd digit sum.
# Sample Input: [1234,5678,2468]


numbers = [1234,5678,2468]
result = []
for num in numbers:
    temp = num
    even_sum = 0
    odd_sum = 0
    while temp > 0:
        digit = temp % 10

        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        temp //= 10
    result.append([num, even_sum, odd_sum])

print(result)