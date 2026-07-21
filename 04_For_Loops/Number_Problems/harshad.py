
num = 18
sum = 0
for i in str(num):
    sum += int(i)
print("harshad" if num % sum == 0 else "not harshad")

# convert number to a string so we can look at each digit.
#loops over each character in "18" one by one
# sum +=int(i) sum = 0+1
#convert i into int so that we can add each digit in each loop
#to get the sum of digits
