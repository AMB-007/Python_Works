#Count the occurrence of a given character.Sample Input: String=programming, Character=g
text = "programming"
char = "g"
count = 0;
for i in text:
    if i == char:
        count += 1
print(count)
    