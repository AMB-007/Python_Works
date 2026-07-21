# Q17. Print the frequency of every element in a list without using a dictionary
# Input: [2,3,2,4,3,2]

numbers = [2, 3, 2, 4, 3, 2]
checked = []

for num in numbers:
    if num not in checked:
        count = 0
        for n in numbers:
            if n == num:
                count += 1
        print(f"{num} -> {count} time(s)")
        checked.append(num)
