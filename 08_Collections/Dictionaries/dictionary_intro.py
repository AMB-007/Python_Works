# eleemnts in a dictionary should be in {key:value} pair

# duplicates keys are not allowed in dictionary

# dictionary is mutable

# no index positioning

# dictionary is iterable(iterable through keys)

# key must be in string or integer datatype



elements = {"age":23,"name":"arun","place":"kochi"}

print(elements["name"]) # return the value of key given

elements["course"] = "python" # if the key is not present in dictionary,it accepts the key,value pair

for i in elements:

    print(elements[i]) # i carries key

# Methods

elements.clear()
elements.pop("name")
elements.popitem()
elements.keys()
elements.values()
elements.get("name") # return the value of key given if it exists else return none value