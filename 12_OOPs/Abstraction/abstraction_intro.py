# Question: Demonstrate Abstraction in Python using the abc module and @abstractmethod decorator.

"""
Abstraction:
The concept of hiding internal implementation details and showing only essential features to the user.
Achieved in Python using the ABC (Abstract Base Class) module and @abstractmethod decorator.
"""

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def display_message(self):
        pass

class ChildClass(AbstractClass):
    def display_message(self):
        print("Hello World - Implemented Abstract Method")

# Instantiate child class and invoke method
obj = ChildClass()
obj.display_message()
