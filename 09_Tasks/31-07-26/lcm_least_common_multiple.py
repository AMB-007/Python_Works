# Question: Write a Python program to calculate the Least Common Multiple (LCM) of two numbers.

num_1 = 8
num_2 = 12

# Formula: LCM(a,b) = (a * b) / GCD(a,b)
max_num = max(num_1, num_2)
lcm = max_num

while True:
    if lcm % num_1 == 0 and lcm % num_2 == 0:
        break
    lcm += max_num

print(f"LCM of {num_1} and {num_2} =", lcm)
