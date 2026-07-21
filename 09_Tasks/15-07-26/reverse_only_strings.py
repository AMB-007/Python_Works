# Reverse Only the Strings
# Reverse only string elements; keep numbers unchanged.
# Sample Input: ['python',10,'django',20,'AI']


text = ['python', 10, 'django', 20, 'AI']

result = []

for i in text:
    if str(i).isdigit():
        result.append(i)
    else:
        result.append(i[::-1])

print(result)