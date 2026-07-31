# Question: Given text = 'ABABC', print the first non-repeating character without using a nested loop.

text = "ABABC"

# Build frequency map using a single pass (dictionary)
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

# Find first character with count == 1
first_non_repeating = None
for char in text:
    if freq[char] == 1:
        first_non_repeating = char
        break

print(f"Text: '{text}' | First non-repeating character:", first_non_repeating)
