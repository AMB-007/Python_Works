# Question: Write a Python program for reverse string.

def reverse(text):
    rev = ""
    for i in range(len(text)-1,-1,-1):
        rev +=  text[i]
    print(rev)
reverse("Python")
