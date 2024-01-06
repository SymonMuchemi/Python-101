#!/usr/bin/python3
"""Simple program to illustrate the use of the __slots__ 
    special attribute in python classes
"""

class Student:
    __slots__ = ('Name', 'Age', 'Registration_Number')

    def __init__(self, name, age, regNo):
        self.Name = name
        self.Age = age
        self.Registration_Number = regNo

# Creating an instance of the class
std1 = Student("Symon Muchemi", 21, 1020)
std1 = Student("Jane Doe", 15, 2301)

# Trying to add an attribute to the Student class
try:
    std1.grade = "A"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
