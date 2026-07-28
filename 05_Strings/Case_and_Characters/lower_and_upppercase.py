# Count uppercase and lowercase letters in a string

text = "ProGraMMinGLanGUAge"
lower_count = 0
upper_count = 0

for ch in text:
    if ch.isupper():
        upper_count += 1
    else:
        lower_count += 1

print("Uppercase count:", upper_count)
print("Lowercase count:", lower_count)
