# ============================================================
#  TOPIC: Patterns (Star / Number Patterns)
# ============================================================

# DEFINITION:
#   Pattern programs use nested loops to print shapes made of
#   characters (*, numbers, letters) in a specific arrangement.
#   The outer loop controls the ROWS, inner loop controls COLUMNS.

# RULE OF THUMB:
#   Outer loop → number of rows
#   Inner loop → number of items per row
#   end=""     → stay on the same line
#   print()    → move to the next line (after inner loop)

# ── 1. RIGHT TRIANGLE (Star) ──────────────────────────────
#   *
#   * *
#   * * *
#   * * * *

n = 4
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# ── 2. INVERTED RIGHT TRIANGLE ────────────────────────────
#   * * * *
#   * * *
#   * *
#   *

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# ── 3. NUMBER TRIANGLE ────────────────────────────────────
#   1
#   1 2
#   1 2 3

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# ── 4. PYRAMID (Centered) ─────────────────────────────────
#      *
#     ***
#    *****

for i in range(1, n + 1):
    print(" " * (n - i), end="")    # spaces before
    print("*" * (2 * i - 1))        # stars

# ── 5. INVERTED PYRAMID ───────────────────────────────────
#    *****
#     ***
#      *

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))

# ── 6. DIAMOND ────────────────────────────────────────────
#      *
#     ***
#    *****
#     ***
#      *

# Upper half:
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Lower half:
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# ── 7. RECTANGLE ──────────────────────────────────────────
# * * * * *
# * * * * *
# * * * * *

rows, cols = 3, 5
for i in range(rows):
    print("* " * cols)

# ── 8. HOLLOW RECTANGLE ───────────────────────────────────
# * * * * *
# *       *
# * * * * *

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# KEY POINTS:
#   → Outer loop = rows, inner loop = columns (always)
#   → print(end="") prevents automatic newline
#   → print() with no args prints a blank line (moves to next row)
#   → Spaces before stars create the centered/pyramid effect
#   → String repetition: "*" * 3 = "***", " " * 2 = "  "
