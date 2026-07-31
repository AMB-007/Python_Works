# Question: Write a function that capitalizes the first and fourth letters of a name (e.g., 'macdonald' -> 'MacDonald').

def capitalize_first_and_fourth(name: str) -> str:
    if len(name) < 4:
        return name.capitalize()
    return name[0].upper() + name[1:3].lower() + name[3].upper() + name[4:].lower()

# Test cases
print("Result for 'macdonald':", capitalize_first_and_fourth("macdonald"))
print("Result for 'python':", capitalize_first_and_fourth("python"))
