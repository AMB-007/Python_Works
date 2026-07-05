# wap to print the vowels in the stirng enter by user

text = input("enter the text :")
vowels = "AEIOUaeiou"
new = ""
#count = 0
for i in text:
    if i  in vowels:
        #count += 1
        new += i
        print(new)
