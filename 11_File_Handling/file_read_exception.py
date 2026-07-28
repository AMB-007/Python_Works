# filename = input("Enter file name :")
# try:
#     file = open(filename,"r")
#     result = file.read()
#     print(result)
# except FileNotFoundError:
#     print("Enter the correct filename")
# print("Thankyou")


# in "r" mode if the file dosent exist it will raise a exception FileNotError



# file = open("git.txt","w")
# file.write("Hello world")
# file.close()

"""
"w" mode used to write a file
in " w" mode if the given filename is existiing it overwrite all the content and write the given data

if the file dosent exist it will create a new file and weite the content given

"""


# file = open("C:/Vs code/Python_Works/25-07-26/File Handling/new.txt","w")
# file.write("Hello world hello")
# file.close()



# file = open("C:/Vs code/Python_Works/25-07-26/File Handling/new.txt","a")
# file.write("Hello world hello Thank You")
# file.close()


"""
using append mode it cannot overwrite the content in given file
just append the content with the existiing  data in the file given

"""


# the file automaticslly closed when the block exits using with keyword
with open("new_1.txt","w")as file:
    file.write("Hello, Python !")

"""
readable() used to check the file is able to read or not
readline()  reade a single line at a time
readlines() read all the lines and add each lines as a element in list and return the list
"""
