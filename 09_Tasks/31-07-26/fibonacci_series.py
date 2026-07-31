# Question: Write a Python program to generate and print the Fibonacci series up to N terms.

terms = 10
a, b = 0, 1

print(f"Fibonacci series ({terms} terms):")
print(a, b, end=" ")

for _ in range(3, terms + 1):
    c = a + b
    a, b = b, c
    print(c, end=" ")
print()
