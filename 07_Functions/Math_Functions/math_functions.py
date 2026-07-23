# ============================================================
#  TOPIC: Functions — Math / Special Numbers
# ============================================================

# DEFINITION:
#   Special numbers have unique mathematical properties.
#   These are classic problems solved using functions.

# ── PRIME NUMBER ──────────────────────────────────────────
# DEFINITION: A number greater than 1 that is divisible ONLY
#             by 1 and itself. (2, 3, 5, 7, 11, 13...)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):   # only check up to √n
        if n % i == 0:
            return False
    return True

print(is_prime(7))    # True
print(is_prime(12))   # False
print(is_prime(1))    # False

# WHY √n?  If n has a factor > √n, it must also have one < √n.
# So we only need to check up to √n.

# ── ARMSTRONG NUMBER ──────────────────────────────────────
# DEFINITION: A number equal to the sum of its own digits
#             each raised to the power of the number of digits.
# Example: 153 → 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓
# Example: 370 → 3³ + 7³ + 0³ = 27 + 343 + 0 = 370 ✓

def is_armstrong(n):
    digits = len(str(n))
    total = sum(int(d) ** digits for d in str(n))
    return total == n

print(is_armstrong(153))    # True
print(is_armstrong(370))    # True
print(is_armstrong(123))    # False

# All 3-digit Armstrong numbers:
armstrong_nums = [n for n in range(100, 1000) if is_armstrong(n)]
print(armstrong_nums)   # [153, 370, 371, 407]

# ── PERFECT NUMBER ────────────────────────────────────────
# DEFINITION: A number equal to the sum of all its proper
#             divisors (divisors excluding the number itself).
# Example: 6  → divisors: 1, 2, 3 → 1+2+3 = 6 ✓
# Example: 28 → divisors: 1,2,4,7,14 → sum = 28 ✓

def is_perfect(n):
    if n < 2:
        return False
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

print(is_perfect(6))     # True
print(is_perfect(28))    # True
print(is_perfect(12))    # False

# ── FACTORIAL (non-recursive) ─────────────────────────────
# DEFINITION: n! = 1 × 2 × 3 × ... × n
#             0! = 1 (by definition)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))     # 120
print(factorial(0))     # 1

# Using math module:
import math
print(math.factorial(6))   # 720

# ── FINDING DIVISORS ──────────────────────────────────────
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

print(get_divisors(12))    # [1, 2, 3, 4, 6, 12]

# KEY POINTS:
#   → Prime: check divisibility up to √n only (efficient)
#   → Armstrong: convert number to string to get individual digits
#   → Perfect: sum proper divisors (1 to n-1), exclude n itself
#   → All three use the same core idea: loop + condition + check
