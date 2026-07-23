# ============================================================
#  TOPIC: Conversions in Python
# ============================================================

# DEFINITION:
#   Conversions means changing a value from one unit or type
#   to another — either unit conversions (e.g. °C to °F) or
#   type conversions (e.g. string to integer).

# ── TYPE CONVERSIONS (Casting) ────────────────────────────
#   int(x)    → converts x to integer     : int("5") = 5
#   float(x)  → converts x to float       : float("3.14") = 3.14
#   str(x)    → converts x to string      : str(100) = "100"
#   bool(x)   → converts x to boolean     : bool(0) = False

# EXAMPLES – Type Conversion:
age = int(input("Enter age: "))        # input() always returns str
price = float(input("Enter price: "))  # convert to float for decimals
print(str(age) + " years old")         # convert back to str for joining

# ── UNIT CONVERSIONS ─────────────────────────────────────

# Celsius to Fahrenheit:  F = (C × 9/5) + 32
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)    # 98.6

# Fahrenheit to Celsius:  C = (F - 32) × 5/9
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(round(celsius, 1))    # 37.0

# Years to Days:
years = 3
days = years * 365
print(days)    # 1095

# Total Seconds → Days, Hours, Minutes, Seconds:
total_seconds = 100000
days    = total_seconds // 86400       # 86400 = 24*60*60
remaining = total_seconds % 86400
hours   = remaining // 3600
remaining = remaining % 3600
minutes = remaining // 60
seconds = remaining % 60
print(f"{days}d {hours}h {minutes}m {seconds}s")

# KEY POINTS:
#   → input() always returns a STRING — always convert it
#   → int() truncates decimals: int(3.9) = 3
#   → Use round() to control decimal places in float results
