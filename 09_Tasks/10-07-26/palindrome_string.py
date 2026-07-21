def palindrome(text):
    rev = ""

    i = len(text) - 1

    while i >= 0:
        rev += text[i]
        i -= 1

    if text == rev:
        return "Palindrome"
    else:
        return "Not Palindrome"


text = input("Enter a string: ")

print(palindrome(text))