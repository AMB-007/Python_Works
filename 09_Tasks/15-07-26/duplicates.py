# Remove Duplicate Strings (Ignore Case)
# Sample Input: ['Python','java','PYTHON','Java','C','c']


text = ['Python', 'java', 'PYTHON', 'Java', 'C', 'c']

result = []

for i in text:
    if i.lower() not in [j.lower() for j in result]:
        result.append(i)

print(result)