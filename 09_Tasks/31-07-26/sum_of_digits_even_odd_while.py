# Question: Calculate sum of digits of a positive integer using a while loop. Check if sum is even or odd.

num = int(input("Enter a positive integer: "))
temp = abs(num)
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

print(f"Sum of digits of {num} = {digit_sum}")

if digit_sum % 2 == 0:
    print("Sum is Even")
else:
    print("Sum is Odd")
