# Swapcase string manually using isupper() and islower()

text = "PyThon"
new_text = ""

for ch in text:
    if ch.isupper():
        new_text += ch.lower()
    else:
        new_text += ch.upper()

print("Original:", text)
print("Swapped:", new_text)
