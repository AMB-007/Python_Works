# merge these  two list without duplicates

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]


list3 = list1 + list2
print(list)
new = []

for i in list3:
    if i not in new:
        new.append(i)
print(new)