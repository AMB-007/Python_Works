# ============================================================
#  TOPIC: Operators in Python
# ============================================================

# DEFINITION:
#   Operators are special symbols that perform operations
#   on values (operands). Python has several categories.

# ── 1. ARITHMETIC OPERATORS ──────────────────────────────
#   +   Addition        : 10 + 3 = 13
#   -   Subtraction     : 10 - 3 = 7
#   *   Multiplication  : 10 * 3 = 30
#   /   Division        : 10 / 3 = 3.333...
#   //  Floor Division  : 10 // 3 = 3
#   %   Modulus         : 10 % 3 = 1
#   **  Exponent        : 2 ** 3 = 8

# ── 2. COMPARISON OPERATORS ──────────────────────────────
#   ==   Equal to             : 5 == 5  → True
#   !=   Not equal to         : 5 != 3  → True
#   >    Greater than         : 7 > 3   → True
#   <    Less than            : 3 < 7   → True
#   >=   Greater than or equal: 5 >= 5  → True
#   <=   Less than or equal   : 3 <= 5  → True
#   Result is always True or False (boolean)

x, y = 10, 3
print(x == y)    # False
print(x > y)     # True
print(x != y)    # True

# ── 3. ASSIGNMENT OPERATORS ──────────────────────────────
#   =    Assign          : x = 5
#   +=   Add & assign    : x += 3   → x = x + 3
#   -=   Sub & assign    : x -= 3   → x = x - 3
#   *=   Mul & assign    : x *= 2   → x = x * 2
#   /=   Div & assign    : x /= 2   → x = x / 2
#   //=  Floor & assign  : x //= 2  → x = x // 2
#   **=  Power & assign  : x **= 2  → x = x ** 2
#   %=   Mod & assign    : x %= 3   → x = x % 3

n = 10
n += 5      # n is now 15
n -= 3      # n is now 12
n *= 2      # n is now 24

# ── 4. LOGICAL OPERATORS ─────────────────────────────────
#   and  → True if BOTH conditions are True
#   or   → True if AT LEAST ONE condition is True
#   not  → reverses the boolean value

age = 20
has_id = True
print(age >= 18 and has_id)   # True  (both true)
print(age < 18 or has_id)     # True  (one is true)
print(not has_id)             # False (reversed)

# ── 5. MATH MODULE ───────────────────────────────────────
import math
print(math.sqrt(25))     # 5.0   → square root
print(math.pow(2, 3))    # 8.0   → 2^3
print(math.ceil(4.2))    # 5     → round UP
print(math.floor(4.9))   # 4     → round DOWN
print(math.pi)           # 3.14159...
print(abs(-7))           # 7     → absolute value

# ── SWAP TWO NUMBERS ────────────────────────────────────
a, b = 5, 10

# Method 1: using temp variable
temp = a
a = b
b = temp

# Method 2: Python shorthand (best)
a, b = b, a

# Method 3: using XOR (bitwise)
a = a ^ b
b = a ^ b
a = a ^ b

# KEY POINTS:
#   → % (modulus) is used to check even/odd: n % 2 == 0 → even
#   → // gives integer result regardless of operand types
#   → ** is Python's power operator, not ^ (^ is XOR)
