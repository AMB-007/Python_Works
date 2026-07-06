# print every second character

text = "Python"  # y h n
new = "" 
for i in text:
    if text.index(i) %2 != 0:
        new += i
print(new)
