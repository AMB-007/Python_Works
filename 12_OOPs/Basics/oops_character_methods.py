# Question: Create a Character class with method_1 to count character frequency and method_2 to return unique characters.

class Character:
    def count_characters(self, text):
        return {ch: text.count(ch) for ch in text}

    def get_unique_characters(self, text):
        return set(text)

# Object creation and method testing
obj = Character()
print("Character counts:", obj.count_characters("programming"))
print("Unique characters:", obj.get_unique_characters("programming"))
