# Question: Write a Python program to split a total bill amount equally among a group of people.

total_bill = float(input("Ask the bill amount:"))
people = int(input("Enter the number of peoples:"))

split_amount = total_bill / people
print("Split amount for each person",(split_amount))
