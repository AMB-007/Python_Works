# Count Different Types of Elements (Use type())
# Given a mixed list, use type() to identify each element. If it is a string, further classify it
# using isalpha(), isdigit(), or special character checks. Count alphabets, digits, and
# special characters.
# Sample Input: ['A','5','@','b','9','#','Z']


items = ['A','5','@','b','9','#','Z']
count = {"Alphabets":0,"Digits":0,"Special":0}

for i in items:
    if type(i) == str:
        if i.isalpha():
            count["Alphabets"] += 1
        elif i.isdigit():
            count["Digits"] += 1
        else:
            count["Special"] += 1
print(count)