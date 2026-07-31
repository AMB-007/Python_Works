# Question: Write a Python program to print characters of a string at odd index positions (e.g. name = 'python' -> 'y', 'h', 'n').

name = input("Enter string (e.g. 'python'): ")
odd_position_chars = [name[i] for i in range(1, len(name), 2)]

print("Characters at odd index positions:", " ".join(odd_position_chars))
