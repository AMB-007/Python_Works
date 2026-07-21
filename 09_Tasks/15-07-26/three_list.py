# Split a Mixed List into Three Lists (Use type())
# Use type() to separate integers, strings, and special-character strings.
# Sample Input: [10,'python','@',20,'#','AI','$',15]



text = [10, 'python', '@', 20, '#', 'AI', '$', 15]

integers = []
strings = []
special = []

for i in text:
    if type(i) == int:
        integers.append(i)
    elif type(i) == str:
        if i.isalpha():
            strings.append(i)
        else:
            special.append(i)

print("Integers :", integers)
print("Strings  :", strings)
print("Special  :", special)