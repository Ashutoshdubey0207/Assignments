'''Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.'''
# Ans => a class is an abstract blueprint or logical template, whereas an object is a physical, concrete instance created from that blueprint
# Eg of class = Dog, car, Cat
# Eg of object = Object describes the properties like brown, white , bulldog

'''Q2. Name the four pillars of OOPs.'''
# Ans => Here are four major pillars in oops.Inheritance, Polymorphism, Encapsulation and Abstraction.

'''Q3. Explain why the __init__() function is used. Give a suitable example.'''

'''The __init__() function is the standard constructor method in Python classes.
the __init__() Function is UsedInitializes objects: 
It runs automatically when you create a new instance of a class.
Assigns values: It sets initial values to object properties (attributes).
Sets up state: It performs any startup operations the object needs before use.
Accepts arguments:It allows you to pass unique data directly into the object during creation.'''

'''Q4. Why self is used in OOPs?'''

'''In object-oriented programming (specifically languages like Python), 
self represents the specific object or instance currently calling a method. 
It allows each object to access and control its own unique data and variables 
separate from other objects created from the same class'''

'''Q5. What is inheritance? Give an example for each type of inheritance.'''
#Inheritance is a core concept in Object-Oriented Programming (OOP) that allows a new class (child or derived class) 
# to adopt the attributes and methods of an existing class (parent or base class). 

# Single Inheritance
class parents_class:
    def parent_feature(self):
        return "Parents feature"

class child_class(parents_class):
    def child_feature(self):
        return "Child feature"

obj = child_class()
print(obj.parent_feature())

# Multiple Inhertance
class father:
    def father(self):
        return "I am your father."
class mother:
    def mother(self):
        return "I am your mother."
class child(mother,father):
    def child():
        return "I am their child."

object = child()
print(object.mother())
print(object.father())

# Multilevel Inheritance
class grandFather:
    def grandFather(self):
        return 'I am your Grandfather'
class father(grandFather):
    def father():
        return 'I am your father.'
class child1(father):
    def child():
        return 'I am child.'

new_object = child1()
print(new_object.grandFather())

# Hierarchicalf Inheritance

class vehicle:
    def fuel(self):
        return "As a vehicle I consumes fuel."
class car(vehicle):
    pass
class truck(vehicle):
    pass

obj_3 = truck()
print(obj_3.fuel())

# Hybrid Inheritance
class School:
    def school(self):
        return "This is my school"

class Teacher(School):
    def teacher(self):
        return "I am a teacher"

class Student(School):
    pass

class TeachingAssistant(Teacher, Student):
    pass
obj = Teacher()
print(obj.school())