#Remove all spaces from a string.Sample Input: Python is easy

text = "Python is easy"
new = ""
for i in text:
    if i != " ":
        new += i
print(new)
