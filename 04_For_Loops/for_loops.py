# ============================================================
#  TOPIC: For Loops
# ============================================================

# DEFINITION:
#   A for loop repeats a block of code a fixed number of times,
#   iterating over a sequence (list, string, range, etc.).
#   Use it when you KNOW how many times to repeat.

# SYNTAX:
#   for variable in sequence:
#       # body

# ── RANGE FUNCTION ────────────────────────────────────────
# range(stop)           → 0 to stop-1
# range(start, stop)    → start to stop-1
# range(start, stop, step) → start to stop-1, jumping by step

for i in range(5):          # 0 1 2 3 4
    print(i, end=" ")

for i in range(1, 6):       # 1 2 3 4 5
    print(i, end=" ")

for i in range(1, 11, 2):   # 1 3 5 7 9  (odd numbers)
    print(i, end=" ")

for i in range(10, 0, -1):  # 10 9 8 7... 1  (countdown)
    print(i, end=" ")

# ── ITERATING OVER SEQUENCES ──────────────────────────────

# Over a list:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Over a string:
for char in "Python":
    print(char)     # P y t h o n

# Over a string with index:
s = "hello"
for i in range(len(s)):
    print(i, s[i])  # 0 h, 1 e, ...

# ── NUMBER PROBLEMS ───────────────────────────────────────

# Sum of 1 to n:
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)         # 55

# Multiplication table:
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# FizzBuzz (classic):
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Factorial (n! = 1 × 2 × ... × n):
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)   # 120

# ── SPECIAL NUMBERS ───────────────────────────────────────

# Armstrong number: sum of digits^n == number
n = 153
digits = len(str(n))
total = sum(int(d) ** digits for d in str(n))
print("Armstrong:", total == n)    # True

# Perfect number: sum of divisors == n (e.g., 6 = 1+2+3)
n = 6
total = sum(i for i in range(1, n) if n % i == 0)
print("Perfect:", total == n)      # True

# Prime number: divisible only by 1 and itself
n = 29
is_prime = all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print("Prime:", is_prime)          # True

# ── break / continue / else ───────────────────────────────
for i in range(1, 6):
    if i == 3:
        break           # stops at 3 → prints 1 2
    print(i)

for i in range(1, 6):
    if i == 3:
        continue        # skips 3 → prints 1 2 4 5
    print(i)

# else with for: runs if loop completed WITHOUT break
for i in range(2, 10):
    if 10 % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

# KEY POINTS:
#   → range() generates numbers but doesn't store them (memory efficient)
#   → Use enumerate(lst) to get index + value together
#   → Use zip(a, b) to loop over two lists simultaneously
#   → for..else is unique to Python — else runs only if no break occurred
