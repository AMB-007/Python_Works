# Question: Write a Python program to find and print all prime numbers below N, where N is entered by user.

n = int(input("Enter N: "))
primes = []

for num in range(2, n):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(f"Prime numbers below {n}:", primes)
