# Question: Calculate the sum of all odd numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for num in numbers:
    if num % 2 != 0:
        total += num

print("Sum of odd numbers in list:", total)

