# Extract and print only lowercase letters from a string

text = "ProGraMMinGLanGUAge"
lowercase_chars = ""

for ch in text:
    if ch.islower():
        lowercase_chars += ch

print("Filtered lowercase characters:", lowercase_chars)
