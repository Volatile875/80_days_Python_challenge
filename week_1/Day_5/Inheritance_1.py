# Inheritance in oob concept in which i child class gains the characterstics or behaviour of it's parent class.

#Q. Create a class named Person, with first name and last name properties, and a print name method:




from calendar import c
from sys import stderr
from xml.sax.handler import feature_namespace_prefixes


class Plank:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)

p1=Plank("Jhon","doc")
p1.printname


'''NOTE= use the pass kwyword, when you do not want to add any other properties or methods to the class'''

#Adding __init__function ; Note: the child __init__ function outside the inheritance of he parent's __init__() function.
#example=

class max:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Level(max):
    def __init__(self, name, age):
        super().__init__(name, age)

#Super Function:
#python also has a super() function that will make the child class inherit all the method and the properties from it's parent.

# class student():
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)


#addmethod(); after using super()=

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()