#Print the difference between every pair of consecutive prime numbers from 1 to N.
n = 20
prev = 0

for i in range(2, n + 1):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2:
        if prev != 0:
            print(i - prev)
        prev = i