# ============================================================
#  TOPIC: Functions — Recursion
# ============================================================

# DEFINITION:
#   Recursion is when a function CALLS ITSELF to solve a smaller
#   version of the same problem. Every recursive function needs:
#     1. BASE CASE   → condition to STOP (prevents infinite loop)
#     2. RECURSIVE CASE → the function calling itself with smaller input

# HOW IT WORKS:
#   factorial(3)
#     → 3 * factorial(2)
#          → 2 * factorial(1)
#               → 1 * factorial(0)
#                    → returns 1  ← BASE CASE
#               ← returns 1 * 1 = 1
#          ← returns 2 * 1 = 2
#     ← returns 3 * 2 = 6

# SYNTAX:
#   def func(n):
#       if base_condition:          # BASE CASE
#           return base_value
#       return func(smaller_n)      # RECURSIVE CALL

# ── FACTORIAL ─────────────────────────────────────────────
# n! = n × (n-1)!    Base: 0! = 1

def factorial(n):
    if n == 0 or n == 1:    # BASE CASE
        return 1
    return n * factorial(n - 1)  # RECURSIVE CALL

print(factorial(5))    # 120  (5×4×3×2×1)
print(factorial(0))    # 1
print(factorial(1))    # 1

# ── FIBONACCI SERIES ──────────────────────────────────────
# F(0)=0, F(1)=1, F(n) = F(n-1) + F(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21...

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))    # 13

# ── SUM OF N NUMBERS ──────────────────────────────────────
# sum(n) = n + sum(n-1)    Base: sum(0) = 0

def sum_n(n):
    if n == 0:              # BASE CASE
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))    # 15  (5+4+3+2+1+0)

# ── POWER (x^n) ───────────────────────────────────────────
# x^n = x × x^(n-1)    Base: x^0 = 1

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print(power(2, 5))    # 32

# ── REVERSE A STRING ──────────────────────────────────────
def reverse_str(s):
    if len(s) == 0:         # BASE CASE
        return ""
    return s[-1] + reverse_str(s[:-1])

print(reverse_str("hello"))    # olleh

# ── RECURSION vs ITERATION ────────────────────────────────
# Recursive factorial:        Iterative factorial:
#   def fact(n):                def fact(n):
#       if n == 0: return 1         result = 1
#       return n * fact(n-1)        for i in range(1,n+1):
#                                       result *= i
#                                   return result

# WHEN TO USE RECURSION:
#   ✔ Problems naturally divide into smaller sub-problems
#   ✔ Tree/graph traversal, divide-and-conquer algorithms
#   ✘ When iteration is simpler and more efficient
#   ✘ Deep recursion can hit Python's limit (default ~1000 calls)

# KEY POINTS:
#   → ALWAYS define a BASE CASE — without it, infinite recursion crashes
#   → Each recursive call must move CLOSER to the base case
#   → Python's recursion limit: sys.getrecursionlimit() → 1000
#   → Recursion uses the call stack — each call adds a frame
