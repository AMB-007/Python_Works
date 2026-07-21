def count_words(text):
    words = text.split()
    return len(words)


text = input("Enter a sentence: ")

print("Number of Words =", count_words(text))