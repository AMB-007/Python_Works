# Rotate a list right by K positions using insert(0, pop())

numbers = [1, 2, 3, 4, 5]
k = 3

for i in range(k):
    numbers.insert(0, numbers.pop())

print(f"List after rotating right by {k} positions:", numbers)
