#!/usr/bin/python3
"""simple program to illustrate the use of __dict__ attribute
    """

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# instatiation
person = Person("John", 87)

# Accessing attributes
print(person.__dict__)

# Modifying attributes dynamically using __dict__
person.__dict__["gender"] = "Male"
print(person.__dict__)

# Deleting an attribute using __dict__
del person.__dict__["age"]
print(person.__dict__)
