def even_index(text):
    result = ""

    for i in range(0, len(text), 2):
        result += text[i] + " "

    return result


text = input("Enter a string: ")

print("Even Index Characters:", even_index(text))