def remove_digits(text):
    result = ""

    for ch in text:
        if not ch.isdigit():
            result += ch

    return result


text = input("Enter a string: ")

print("After Removing Digits:", remove_digits(text))