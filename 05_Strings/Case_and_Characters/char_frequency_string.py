# Question: Write a Python program to count character frequency and format output with counts.

text = "programming" # output = p1r2o1g2a1m2i1n1
new = ""
for i in text:
    if i not in new:
        new += i + str(text.count(i))

print(new)

