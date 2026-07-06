# Count the number of digits in a string.Sample Input: Abc12345
text = "Abc12345"
count = 0
for i in text:
    if i.isdigit():
        count += 1
print(count)
    
