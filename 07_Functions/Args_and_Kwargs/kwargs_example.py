#functions

 #positional
 #keyword
 #default
 

def sum_numbers(**kwargs):
    print(kwargs)

sum_numbers(a=1,b=3,c=5)

#**kwargs allows the user the function to accept the variables count of keyword arguments in each function call
# it colects all the keyword arguments in a dictionary