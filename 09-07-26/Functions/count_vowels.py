#define a function to get the total number of vowels in thre string enter by user

def vowel(ch):
    count = 0
    vowels = "aeiouAEIOU"

    for char in ch:
        if char in vowels:
            count += 1

    print("Total vowels:", count)

text = input("Enter a string: ")
vowel(text)