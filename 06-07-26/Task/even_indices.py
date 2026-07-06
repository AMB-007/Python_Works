#Print characters at even indices.Sample Input: Python
text = "Python"
new = ""
for i in range(len(text)):
    if i %2 == 0:
        new += text[i]
print(new)
