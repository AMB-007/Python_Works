#Print only numeric characters from a string.Sample Input: Ab12Cd345

text = "Ab12Cd345"

for i in text:
    if i.isdigit():
        print(i, end="")