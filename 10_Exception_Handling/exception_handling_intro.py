"""
wap to get division of two numbers
#Expection Handling
==================

Expection is thr error occuring during the runtime(progm is running)
while getting an expection python stop the execution abruptly and getting a traceback



by expection handling

program start  >>> expection occurs >>> Expection can be handled >>> program continues
"""


# num_1 = int(input("enter a number"))
# num_2 = int(input("Enter a number"))

# try:
#     result = num_1 / num_2
#     print(result)
#     # try block used to keep the risky code(where expection may occur during runtime)
# except:
#     print("zero division not possible")
#     # Expect block runs only if any execution occurs in try block

# print("end")






# try:
#     num_1 = int(input("enter a number :"))
#     print(100/num_1)
# except ZeroDivisionError:
#     print("Zero division is not possible")
# except ValueError:
#     print("Enter proper number")
# print("End")

# wap to get the index position from the user and display the element from the list

# words = ["python","b","c","java","e"]
# index = int(input("Enter the number"))
# try:
#     print(words[index])
# except IndexError:
#     print("Enter a proper index position")
# finally:
#     print("Thank U")


#wap to access missing dictionary key and handle the keyerror

# elements = {"name":"arun","age":23,"place":"cochin"}

# key = input("Enter the key")

# try:
#     print(elements[key])
# except KeyError:
#     print("enter a valid key")

# finally:
#     print("Thank u")









"""
raise 
================
used to create a exception manually if it doesnt meet any condition
using raise we can throw custom exceptions during the run time
we can raise Valeerror,IndexError,......
used when we want to stop the execution because a condition is invalid


"""

# age = int(input("Enter age :"))
# if age < 18:
#     raise Exception("Invalid age")
# print("Thankyoou")


"""
assert >>> AssertError
======
used to chcek a condition is True.it the conf=dition is False python automatically raises a AssertError

Used for debugging and unit testing to catch program mistakes

assert Condition ,"Error message"


"""


age = int(input("Enter the age :"))
assert age > 18,'InvalidAge'
print("Thankyoou")