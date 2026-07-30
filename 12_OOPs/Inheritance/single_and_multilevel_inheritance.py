# Question: Demonstrate Single-Level and Multi-Level Inheritance concepts in Python.

"""
Inheritance:
A technique where a child/derived class acquires the properties and methods
of a parent/base class to enable code reusability and relationship hierarchy.

Types of Inheritance:
1. Single-Level Inheritance
2. Multi-Level Inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
"""

# Example 1: Single-Level Inheritance
class Parent:
    def car(self):
        print("Maruti 800")

    def bike(self):
        print("Royal Enfield")

class Child(Parent):  # Inheriting Parent class
    pass

child_obj = Child()
print("Child calling Parent's bike method:")
child_obj.bike()

# Example 2: Multi-Level Inheritance
class ClassA:
    def method_a(self):
        print("Method from Class A")

class ClassB(ClassA):  # Level 1 Inheritance
    def method_b(self):
        print("Method from Class B")

class ClassC(ClassB):  # Level 2 Inheritance
    def method_c(self):
        print("Method from Class C")

c_obj = ClassC()
print("\nMulti-level inheritance call:")
c_obj.method_a()
c_obj.method_b()
c_obj.method_c()
