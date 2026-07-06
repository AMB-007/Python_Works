#  Compress a string (Example: aaabbc -> a3b2c1).Sample Input: aaabbcccc


text = "aaabbcccc"
count = 0
new = ""
for i in text:
    if i not in new:
        new += i
        new += str(text.count(i))
print(new)