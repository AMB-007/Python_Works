def reverse_string(text):
    rev = ""
    i = len(text) - 1

    while i >= 0:
        rev += text[i]
        i -= 1

    return rev


text = input("Enter a string: ")

print("Reversed String =", reverse_string(text))