#Remove all digits from a string.Sample Input: Py123thon45
text = "Py123thon45"
new = "" 
for i in text :
    if i.isalpha() == True:
        new += i
print(new)
