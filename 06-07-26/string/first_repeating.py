# wap to get the first repeating character from the string

# text = "programming"

# for i in text:
#     if text.count(i) > 1:
#         print(i)
#         break 



# wap to get the first two unique characters from the string
text = "programming"
count = 0
for i in text:
    if text.count(i) == 1:
        print(i)
        count += 1
    if count == 2:
        break