# Question: Demonstrate Method Overriding where a child class provides its own specific implementation of a parent method.

"""
Method Overriding:
A feature that lets a child/derived class provide its own specific version of a method
already defined in its parent/base class.
"""

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  # Overriding Parent's greet method
        print("Hello World from Child")

# Invoking overridden method
obj = Child()
obj.greet()
