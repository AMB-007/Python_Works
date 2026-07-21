#  Count the number of uppercase and lowercase letters in a string.Sample Input: PyTHon123

text = "PyTHon123"

upper_count = 0
lower_count = 0

for i in text:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1

print(lower_count)
print(upper_count)




