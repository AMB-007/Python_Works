text = "PyTHon123"
upper_count = 0
lower_count = 0
for i in text:
    if i.isupper():
        upper_count += 1
    else:
        lower_count += 1
print(lower_count)
print(upper_count)