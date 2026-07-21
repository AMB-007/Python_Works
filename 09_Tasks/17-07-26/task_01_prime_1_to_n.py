# Q1. Print all prime numbers between 1 and N
# Sample Input: 20
# Sample Output: 2 3 5 7 11 13 17 19

n = int(input("Enter N: "))

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
