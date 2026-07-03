# wap to print the vowels in the stirng enter by user

text = input("enter the text :")
vowels = "AEIOUaeiou"
count = 0
for i in text:
    if i  in vowels:
        count += 1
        print(i)
print(count)