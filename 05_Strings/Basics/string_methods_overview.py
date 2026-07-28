# Overview of common string methods in Python

text = "python"
print("Uppercase:", text.upper())       # Returns uppercase copy: 'PYTHON'
print("Lowercase:", text.lower())       # Returns lowercase copy: 'python'
print("Capitalize:", text.capitalize()) # Returns capitalized copy: 'Python'
print("Count of 'p':", text.count("p")) # Total occurrences of 'p'
print("Index of 't':", text.index("t")) # Index of first occurrence of 't'
print("Find 'z':", text.find("z"))      # Index of first occurrence or -1 if not found
print("Swapcase:", text.swapcase())     # Converts upper to lower and lower to upper
