# Find the first non-repeating character in a string.Sample Input: swiss

text = "swiss"
for i in text:
    if text.count(i) == 1:
        print(i)
        break

