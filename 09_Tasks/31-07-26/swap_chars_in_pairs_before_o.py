# Question: Find first occurrence of 'o' in a string. Swap characters before 'o' in pairs (e.g. 'hello' -> 'lleho'). Keep remaining string unchanged.

text = input("Enter string (e.g., 'hellopython'): ")

o_index = text.find('o')

if o_index != -1:
    prefix = list(text[:o_index])
    # Swap adjacent characters in pairs
    for i in range(0, len(prefix) - 1, 2):
        prefix[i], prefix[i+1] = prefix[i+1], prefix[i]
    
    result = "".join(prefix) + text[o_index:]
    print("Transformed string:", result)
else:
    print("Character 'o' not found in string.")
