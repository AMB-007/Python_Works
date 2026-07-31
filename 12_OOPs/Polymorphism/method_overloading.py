# Question: Explain Method Overloading concept and Python's behavior regarding multiple methods with the same name.

"""
Method Overloading:
A feature where a class has multiple methods with the same name but different parameter signatures.
Note: Python does NOT natively support method overloading like Java/C++. In Python, defining a method
with the same name replaces the previous definition (the last method definition overrides earlier ones).
"""

class DemoOverload:
    def method_1(self, a, b, c):
        print("Three arguments:", a, b, c)

    # In Python, this second definition overrides the first one
    def method_1(self, name, age):
        print(f"Name: {name}, Age: {age}")

obj = DemoOverload()
obj.method_1("Arun", 23)
