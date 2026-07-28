# Question: write a pyton prgm that takesd a list of integers and performs the following steps:
# rotate the last to right by 2 positions.
# (the last two elements move to front)
# then replace every even number with its half, and every odd number with its double.
# finally print the modified list




numbers = [3, 2, 4, 5, 6, 7, 8]
rotate = numbers[-2:] + numbers[:-2]

new = []

for num in rotate:
    if num % 2 == 0:
        new.append(num // 2)
    else:
        new.append(num * 2)

print(new)
