items = ['apple', 'banana', 'grapes']

freq = []

for word in items:
    largest = 0
    for i in word:
        if word.count(i) > largest:
            largest = word.count(i)
            char = i
    if largest > 1:
        freq.append(char)
print(freq)
