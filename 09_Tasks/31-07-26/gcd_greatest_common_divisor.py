# Question: Write a Python program to calculate the Greatest Common Divisor (GCD) of two numbers.

num_1 = 20
num_2 = 28

gcd = 1
for i in range(1, min(num_1, num_2) + 1):
    if num_1 % i == 0 and num_2 % i == 0:
        gcd = i

print(f"GCD of {num_1} and {num_2} =", gcd)
