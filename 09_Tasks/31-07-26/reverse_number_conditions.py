# Question: Input a positive integer, reverse its digits, and check conditional thresholds (> 500, ends with 0, or neither).

num = int(input("Enter a positive integer: "))
temp = num
reversed_num = 0

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

print(f"Original: {num} | Reversed: {reversed_num}")

if reversed_num > 500:
    print("Reversed Number is Greater than 500")
elif str(reversed_num).endswith('0'):
    print("Reversed Number Ends with 0")
else:
    print("Reversed Number does not meet any condition")
