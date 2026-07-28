# Find the first two unique (non-repeating) characters in a string

text = "programming"
count = 0

for ch in text:
    if text.count(ch) == 1:
        print("Unique character:", ch)
        count += 1
    if count == 2:
        break
