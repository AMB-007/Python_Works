def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for ch in text.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


text = input("Enter a string: ")

v, c = count_vowels_consonants(text)

print("Vowels =", v)
print("Consonants =", c)
