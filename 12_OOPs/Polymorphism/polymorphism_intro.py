# Question: Demonstrate Polymorphism in Python where different classes respond to the same method call.

"""
Polymorphism:
The ability of different object classes to respond to the same method call in their own unique way.
Same method name, but different underlying behavior/implementation.
"""

class ClassA:
    def calculate(self, a, b):
        print("Sum:", a + b)

class ClassB:
    def calculate(self, a, b, c):
        print("Product:", a * b * c)

obj1 = ClassA()
obj2 = ClassB()

obj1.calculate(4, 5)
obj2.calculate(4, 5, 6)
