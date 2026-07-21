# Q13. Print characters at odd index positions
# (index 1, 3, 5, ...)

text = input("Enter a string: ")

print("Characters at odd index positions:")
for i in range(len(text)):
    if i % 2 != 0:
        print(f"Index {i}: {text[i]}")
