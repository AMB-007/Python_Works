n = int(input("Enter the number b/w 10 and 20 :"))

while n <= 10 or n >= 20:
    print("Too Low" if n <= 10 else "Too High")
    n = int(input("Enter the number b/w 10 and 20 :"))
print("Thank You")
