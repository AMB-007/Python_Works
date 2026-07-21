# Q8. Find the sum of odd digits in a number
# Input: 58391   Output: 17  (5 + 3 + 9 = 17)

n     = int(input("Enter a number: "))
total = 0

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        total += digit
    n = n // 10

print("Sum of odd digits:", total)
