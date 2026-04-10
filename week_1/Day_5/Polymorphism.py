# polmorphism means "mayforms" and in programming it refers to method/ fuction/operations with same name executed on many object or classes.

#Duck typing := "if it walks like duck and quacks like a duck, then it is a duck".



class Bird:
    def fly(self):
        print("flying high in the sky")

class Airplane:
    def fly(self):
        print("taking off from the runway")

def lift_off(entity):
    entity.fly()

b = Bird()
a = Airplane()

lift_off(b)
lift_off(a)


print("---------------------------------------------")

# method overloading= but python doesn't because it's dynamically typed it resources method calls at runtime, not during compilation.

# Method Overiding : when a child class provide a specific implemetation for a methods that is alredy defined in it's parent calss, "it overrides"
# --the original method.

class Shape:
    def area (self):
        return "calculationg area...."
class circle(Shape):
    def area(self):
        return "Area = pi * r**2"
class square(Shape):
    def area(self):
        return "Area= side * side"
    
shape=[circle(),square()]
for s in shape:
    print(s.area())




