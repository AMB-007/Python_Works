# Question: Given text = 'ABEABAIACB', print the most recursive (frequent) consonant.

text = "ABEABAIACB"
vowels = "AEIOUaeiou"

consonant_freq = {}
for char in text:
    if char.isalpha() and char not in vowels:
        consonant_freq[char] = consonant_freq.get(char, 0) + 1

most_frequent = max(consonant_freq, key=consonant_freq.get)

print(f"Text: '{text}'")
print(f"Consonant Frequencies: {consonant_freq}")
print("Most frequent consonant:", most_frequent)
