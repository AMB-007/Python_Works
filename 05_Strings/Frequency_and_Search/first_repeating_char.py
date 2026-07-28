# Question: Find the first repeating character in a string

text = "programming"

for ch in text:
    if text.count(ch) > 1:
        print("First repeating character:", ch)
        break

