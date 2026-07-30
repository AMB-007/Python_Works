# Question: Rotate a list right by 2 positions, then replace even numbers with their half and odd numbers with their double.

numbers = [3, 2, 4, 5, 6, 7, 8]
rotate = numbers[-2:] + numbers[:-2]

new = []

for num in rotate:
    if num % 2 == 0:
        new.append(num // 2)
    else:
        new.append(num * 2)

print("Modified list:", new)
