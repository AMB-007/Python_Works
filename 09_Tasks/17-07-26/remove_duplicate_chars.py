# Q12. Remove duplicate characters while maintaining order
# Input: programming   Output: progamin

text   = input("Enter a string: ")
result = ""

for ch in text:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)
