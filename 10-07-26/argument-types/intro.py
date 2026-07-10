def details(name,place,role = "dev"):
    print(f"hii{name}u are frm{place}in u are a {role}")

"""
details("kochi",dev,"arun") # positional arguments
arguments need to be passed in correct sequential order
=========================================================
details(place="kochi",role="dev",name="arun")# keyword argument

u can specify the arguments by using the parameter name along with the value
while using the keyword arguments the order of parameter dosent matter


#Default argument
=================
Assign the default values to the parameter when defining the function
if caller dosent provide the value the default value will be passed into function

"""

details(place="kochi",name="arun",role="testing")