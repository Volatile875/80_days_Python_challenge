# CLASS is a user-defined blueprint or templated used to create objects.
# OBJECTS is entities created inside abstract of class.



from re import X


class Car:
    X=5

# create object

# class MyClass:
#     x = 10

# p1 = MyClass()
# print(p1.x)

# deleting object:
 
# del p1


# __init__ Method: all classes have built-in methods used the objects of a class.

class plan:
    def __init__(self, name, age):
        self.name=name
        self.age=age
ob1=plan("yash",36)
print(ob1.name)
print(ob1.age)

# Self Parameter : The self parameter to the current instance of the class.
# It is used to access properties and methods that belong the classes.

class krap:
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def greet(self):
        print("hello,my name is" + self.name )
p1=krap("yash",24)
p1.greet()

print(p1.name)
print(p1.age)


'''Note: The self parameter must be the first parameter of any method in the class.'''
# without self, python would not know which object properties you want to access.  you can use self with putting different name.

# class leng:
#     def __init__(obj,name,age):
#         obj.name=name
#         obj.age=age

#     def greet(obj):
#         print("hello, my name is ", obj.name)

# p1=leng("emil",36)
# p1.greet()


# print("--------------------------------------------------")


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        return("Hello" + self.name)
    def welcome(self):
        message=self.greet()
        print(message + " Welcome to website ")

p1=Person(" tobi",87)
p1.welcome()


#Class Properties: properties are variables that belong to a class. They store data for end object created from the class.

class lat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=lat("pratik",100)

print(p1.name)
print(p1.age)

print("------------------------------------------------")

# Class vs object properties:
# properties defined inside __init__() belong to each object.(instance_properties)
# Properties defined outside method belong to the class itself and shared by all objects: (class Properties).
# EXAMPLE OF INSTNCE VE CLASS PROPERTIES:


class Wrestler:
    species = "Human"

    def __init__(self, name, player, city):
        self.name = name
        self.player = player
        self.city = city


p1 = Wrestler("RKO", "Randy Orton", "California")

print(p1.name)
print(p1.player)
print(p1.city)


print("---------------------------------------------------")
class people:
    def __init__(self, bablade, owner):
        self.bablade=bablade
        self.owner=owner

    def __str__(self):
        return f"{self.bablade}{self.owner}"
    
p1= people("kartik",36)
print(p1)
