# Q2. Find the factorial of a number using a for loop
# Input: 5   Output: 120

n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} =", factorial)
