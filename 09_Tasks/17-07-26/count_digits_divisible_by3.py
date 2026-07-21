# Q10. Count how many digits are divisible by 3
# Input: 123456789   Output: 3  (3, 6, 9)

n     = int(input("Enter a number: "))
count = 0

while n > 0:
    digit = n % 10
    if digit != 0 and digit % 3 == 0:
        count += 1
    n = n // 10

print("Count of digits divisible by 3:", count)
