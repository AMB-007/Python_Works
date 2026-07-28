# Question: Write a Python program for remove vowels.

def remove_vowel(text):
    vowels = "AEIOUaeiou"
    for ch in text:
        if ch not in vowels:
            print(ch,end="")
remove_vowel("Education")
