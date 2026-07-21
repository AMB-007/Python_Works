def count_vowel(text):
    vowel ="AEIOUaeiou"
    count = 0
    for ch in text:

        if ch in vowel:
            count += 1
    print(count)
count_vowel("Education")
