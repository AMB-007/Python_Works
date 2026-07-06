# wap to get the unique characters from the string joined together

text = "programming"  # output = "programin"
new = ""
count = 0
for i in text:
    if text.count(i) == 1:
        new += i
        count += 1
print(new)
print(count)
