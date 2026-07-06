# Find the first occurrence of a given character.Sample Input: String=programming, Character=r
text = "programming"
char = "r"
count = 0;
for i in text:
    if i == char:
        count += 1
print(count)