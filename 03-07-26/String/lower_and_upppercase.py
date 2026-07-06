# text = "python"
# text.upper # ureturn a copy of string with all letters in upercased
# text.lower # return a copy of string joined in lowercase
# text.capitalize # Python
# text.count("p") # show the count of the letter    ,    returns the total occurnce of the character
# text.index("t") # show the index of the text   ,   returns the index value of the character first occured
# text.find() # returns the index from the first occurence else returns -1
# text.swapcase() # convert upper into lower case and lower case into uppercase
# #isalphs(),isalnum().islower(),isupper().endswith(),




# text = "PyThon"
# new = ""
# for i in text:
#     if i.isupper():
#         new += i.lower()
#     else:
#         new += i.upper()
# print(new)


# wap to get the count of uppercase letters and lowercase from the string below
# text = "ProGraMMinGLanGUAge"

# text = "ProGraMMinGLanGUAge"
# lower_count = 0
# upper_count = 0
# for i in text:
#     if i.isupper():
       
#         upper_count += 1
#     else:

#         lower_count += 1
# print(upper_count)
# print(lower_count)



text = "ProGraMMinGLanGUAge"
new = ""
for i in text:
    if i.islower():
        new += i
print(new)

