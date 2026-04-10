#Encapsulation : it is about protecting data inside a class. It is about protecting data inside a class.


#1. Priate properties: we can properties private by using a double underscore__ prefix.

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.__age=age
# ob1=Person("patrick",25)
# print(ob1.name)
# print(ob1.__age)

#2. To access private property , you can create a getter method,

class Car:
    def __init__(self,brand, model):
        self.brand=brand
        self.__model=model
    def get__model(self):
        return self.__model
p1=Car("Maruti","Auto800")
print(p1.get__model())

#3. Set Private property Value:

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())


#4. Protected properties:
'''note= python also has convections for protected properties
 using a _ single underscore _prefix. '''

class Person:
   def __init__(self,name,age):
      self.name=name
      self._age=age
p1=Person("max", 29)
print(p1.name)
print(p1._age)

#6. Name Mangling: It is how python implements private propertiesand method.

class xmas:
   def __init__(self,name,age):
      self.__name=name
      self.__age=age
p1=xmas("emil",30)

print(p1._xmas__name)
print(p1._xmas__age)