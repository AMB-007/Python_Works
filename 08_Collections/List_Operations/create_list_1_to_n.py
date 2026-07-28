# Create a list of numbers from 1 to N using input and append()

n = int(input("Enter N: "))
numbers = []

for i in range(1, n + 1):
    numbers.append(i)

print("Generated list:", numbers)
