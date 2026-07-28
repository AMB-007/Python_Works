# Question: Write a Python program for patterns.

# ============================================================
#  TOPIC: Patterns (Star / Number Patterns)
# ============================================================

# DEFINITION:
#   Pattern programs use nested loops to print shapes made of
#   characters (*, numbers, letters) in a specific arrangement.
#   The outer loop controls the ROWS, inner loop controls COLUMNS.

# RULE OF THUMB:
#   Outer loop â†’ number of rows
#   Inner loop â†’ number of items per row
#   end=""     â†’ stay on the same line
#   print()    â†’ move to the next line (after inner loop)

# â”€â”€ 1. RIGHT TRIANGLE (Star) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#   *
#   * *
#   * * *
#   * * * *

n = 4
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# â”€â”€ 2. INVERTED RIGHT TRIANGLE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#   * * * *
#   * * *
#   * *
#   *

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# â”€â”€ 3. NUMBER TRIANGLE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#   1
#   1 2
#   1 2 3

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# â”€â”€ 4. PYRAMID (Centered) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#      *
#     ***
#    *****

for i in range(1, n + 1):
    print(" " * (n - i), end="")    # spaces before
    print("*" * (2 * i - 1))        # stars

# â”€â”€ 5. INVERTED PYRAMID â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#    *****
#     ***
#      *

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))

# â”€â”€ 6. DIAMOND â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
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

# â”€â”€ 7. RECTANGLE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# * * * * *
# * * * * *
# * * * * *

rows, cols = 3, 5
for i in range(rows):
    print("* " * cols)

# â”€â”€ 8. HOLLOW RECTANGLE â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
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
#   â†’ Outer loop = rows, inner loop = columns (always)
#   â†’ print(end="") prevents automatic newline
#   â†’ print() with no args prints a blank line (moves to next row)
#   â†’ Spaces before stars create the centered/pyramid effect
#   â†’ String repetition: "*" * 3 = "***", " " * 2 = "  "

