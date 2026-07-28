# Question: Write a Python program for interleave two lists.

char_1 = ["a","b","c"]
char_2 = ["p","q","r","s"]

#output = "apbqcrs"

result = ""

for i in range(len(char_1)):
    result += char_1[i] + char_2[i]


for i in char_2[len(char_1):]:
    result += i

# for i in range(len(char_1), len(char_2)):
#     result += char_2i

print(result)



