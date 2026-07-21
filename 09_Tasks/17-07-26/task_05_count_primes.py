# Q5. Count how many prime numbers are present between 1 and N

n = int(input("Enter N: "))
count = 0

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print(f"Count of prime numbers between 1 and {n}:", count)
