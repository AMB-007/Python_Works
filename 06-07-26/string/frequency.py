# wap to get frequency of a string

text = "programming"
new = ""
for i in text:
    if i not in new:
        print(i,text.count(i))
        new += i

