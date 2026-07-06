# get the character having largest  from the sting

text = "programmming"
largest = 0
element = ""
for i in text:
    if text.count(i) > largest:
        largest = text.count(i)
        element = i
print(element)