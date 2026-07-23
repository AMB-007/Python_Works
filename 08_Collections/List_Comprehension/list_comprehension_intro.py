"""
A way to create lists in python using a single expression
[new_item for item in iterble]
new_item is the transformed value
item comed from iterable
"""
"""
new = []
for i in numbers
    new.append(i**2)
print(new)


"""
number = [1,2,3,4,5,6]
result  = [i ** 2  for i in number]
print(result)



number = [1,2,3,4,5,6]
result  = [i for i in number if i % 2 == 0]
print(result)




word = ["apple","banana","cherry"]   #['Apple', 'Banana', 'Cherry']
result = [i.capitalize() for i in word]
print(result)

#build a list of strings that start with letter "a"
words = ["arun","apple","python","ml","arab"]
result = [i for i in words if i.startswith("a")]
print(result)


# given a list of words, return a list of word length
words = ["arun","apple","python","ml","arab"]
result = [len(i)for i in words ]
print(result)


#create a new list containing only the square of numbers
#thta divisible by 3 from 1 to 20


print([i ** 2 for i in range(1,20)if i % 3 == 0])

# given sentence ,use list compreshesion to build a list of words thta have more that 4 letters
text = "python is a programming language" #["python","is","a","progeamming","language"]
print([i for i in text.split() if len(i) > 4])



words = ["arun","apple","python","ml","arab"]  #{'arun': 4, 'apple': 5, 'python': 6, 'ml': 2, 'arab': 4}
print({i:len(i) for i in words })


name = "programming"  #{'p': 1, 'r': 1, 'o': 1, 'g': 1, 'a': 1, 'm': 1, 'i': 1, 'n': 1}
print({i:name.count(i) for i in name})