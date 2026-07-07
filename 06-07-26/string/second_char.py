# print every second character

text = "Pythontp"  # y h n
new = "" 
for i in range(len(text)):
    if i % 2 != 0:
        new += text[i]
print(new)