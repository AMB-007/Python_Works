def character_index(text):
    result = []

    for i in range(len(text)):
        result.append(str(i) + " " + text[i])

    return result


text = input("Enter a string: ")

output = character_index(text)

for item in output:
    print(item)
    