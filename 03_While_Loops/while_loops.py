# ============================================================
#  TOPIC: While Loops
# ============================================================

# DEFINITION:
#   A while loop repeats a block of code AS LONG AS
#   the given condition remains True.
#   Use it when you don't know in advance how many times
#   the loop will run.

# SYNTAX:
#   while condition:
#       # body — runs repeatedly until condition is False

# ── BASIC WHILE LOOP ──────────────────────────────────────
i = 1
while i <= 5:
    print(i)        # prints 1 2 3 4 5
    i += 1          # IMPORTANT: update variable to avoid infinite loop

# ── break — exit the loop early ───────────────────────────
# Stops the loop immediately, even if condition is still True.
i = 1
while i <= 10:
    if i == 5:
        break       # stops at 5
    print(i)
    i += 1
# Output: 1 2 3 4

# ── continue — skip current iteration ────────────────────
# Skips the rest of the body and goes back to check condition.
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)
# Output: 1 3 5 7 9

# ── NUMBER PROBLEMS with while ────────────────────────────

# Sum of digits: 1234 → 1+2+3+4 = 10
n = 1234
total = 0
while n > 0:
    total += n % 10     # get last digit
    n //= 10            # remove last digit
print("Sum of digits:", total)   # 10

# Reverse a number: 1234 → 4321
n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed:", rev)          # 4321

# Count digits in a number
n = 12345
count = 0
while n > 0:
    count += 1
    n //= 10
print("Digits:", count)          # 5

# ── SPECIAL NUMBERS ───────────────────────────────────────

# Palindrome check (number): same forwards and backwards
n = original = 121
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Palindrome:", original == rev)   # True

# Armstrong number: sum of (each digit ^ number_of_digits) == n
n = 153
original = n
digits = len(str(n))
total = 0
while n > 0:
    total += (n % 10) ** digits
    n //= 10
print("Armstrong:", original == total)  # True (1³+5³+3³ = 153)

# Prime number check
n = 17
i = 2
is_prime = True
while i <= n // 2:
    if n % i == 0:
        is_prime = False
        break
    i += 1
print("Prime:", is_prime)    # True

# KEY POINTS:
#   → Always update the loop variable inside the body (avoid infinite loops)
#   → Use break to exit early, continue to skip an iteration
#   → while is preferred over for when count of iterations is unknown
#   → n % 10 → last digit,  n // 10 → removes last digit
