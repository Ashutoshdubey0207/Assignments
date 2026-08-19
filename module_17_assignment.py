'''Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
and average_of_vehicle.'''
class vehicle:
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.avg_speed = average_of_vehicle
    
'''Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
Create a method named seating_capacity which takes capacity as an argument and returns the name of
the vehicle and its seating capacity.'''

class Car(vehicle):
    def seating_capacity(self,capacity):
        return  self.name_of_vehicle,capacity
new_car = Car("Audi",120,3)
print(new_car.seating_capacity(5))

'''Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.'''
# Ans = Multiple inheritance in Python is an object-oriented programming feature that allows a child class to inherit attributes and methods from more than one parent class. 
# This allows a subclass to combine functionality from diverse sources without duplicating code.
class Device:
    def __init__(self):
        print("Device initialized")

class Camera(Device):
    def __init__(self):
        super().__init__()
        print("Camera initialized")

class Phone(Device):
    def __init__(self):
        super().__init__()
        print("Phone initialized")

# Smartphone inherits from both Camera and Phone
class Smartphone(Camera, Phone):
    def __init__(self):
        super().__init__()  # Triggers the dynamic MRO pipeline
        print("Smartphone initialized")

gadget = Smartphone()
# Output order follows MRO: Device -> Phone -> Camera -> Smartphone

'''Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
class.'''
# getters and setters are methods used to protect, validate, and manage access to an object's private attributes. 
# They ensure data encapsulation, preventing outside code from directly altering internal data without validation.
class Student:
    numberOfStudents = 0

    def __init__(self,name,rollNo,marks):
        self.name = name
        self.rollNo = rollNo
        self.__marks = marks
        self.numberOfStudents = Student.numberOfStudents + 1
        self.numberOfStudents = self.numberOfStudents + 1

    # getter
    def getMarks(self):
        return self.__marks

    # setter
    def setMarks(self,newMarks,passcode):
        if passcode == self.__auth():
            self.__marks = newMarks
        else:
            print("bhag yaha se")

    def __auth(self):
        return "0000"
    def study(self):
        print("I am " + str(self.rollNo)+ " and I am studing")
    def play(self):
        print("I am playing.")


s1 = Student("Mayank",1,90)
s2 = Student("Mayank",2,80)

s1.setMarks(45,"0000")
print(s1.getMarks())


'''Q5.What is method overriding in python? Write a python code to demonstrate method overriding.'''
'''Method overriding in Python is an object-oriented programming concept where a child class provides a specific implementation of a 
method that is already defined in its parent class. When the method is invoked on an instance of the child class, Python executes the child's 
version of the method instead of the parent's. This enables runtime polymorphism and allows you to customize or extend inherited behaviors 
without modifying the parent class code'''

class Parent:
    def present(self):
        return "I am the parent behavior."

class Child(Parent):
    # Overriding the parent method
    def present(self):
        return "I am the customized child behavior."

# Execution
obj = Child()
print(obj.present())