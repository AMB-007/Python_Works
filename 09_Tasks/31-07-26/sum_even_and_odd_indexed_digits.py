# Question: Write a Python program to print sum of even-indexed digits and odd-indexed digits in a given number.

number_str = input("Enter a number: ")

even_idx_sum = 0
odd_idx_sum = 0

for idx, digit_char in enumerate(number_str):
    if digit_char.isdigit():
        digit = int(digit_char)
        if idx % 2 == 0:
            even_idx_sum += digit
        else:
            odd_idx_sum += digit

print(f"Sum of even-indexed digits (index 0, 2, 4...): {even_idx_sum}")
print(f"Sum of odd-indexed digits  (index 1, 3, 5...): {odd_idx_sum}")
