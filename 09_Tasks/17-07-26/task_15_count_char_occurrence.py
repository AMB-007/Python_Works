# Q15. Count occurrences of a given character without using count()

text   = input("Enter a string: ")
char   = input("Enter the character to find: ")
count  = 0

for ch in text:
    if ch == char:
        count += 1

print(f"'{char}' appears {count} time(s) in the string")
