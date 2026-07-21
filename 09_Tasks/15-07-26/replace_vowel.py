#  Replace Every Vowel with '*'
# Sample Input: ['python','education','apple']

text = ['python', 'education', 'apple']
result = []
for word in text:
    new_word = ""
    for i in word:
        if i.lower() in "aeiou":
            new_word += "*"
        else:
            new_word += i
    result.append(new_word)
print(result)