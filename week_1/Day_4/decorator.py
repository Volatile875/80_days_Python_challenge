# Decorators let's add the extre behaviour to a functions, without changing the function's code.
# Defination: a decorator is function that takes another function the takes another functionas input and return a new function.

# represented as basic decorators = define the decorators first, then apply it with @decorator_name above the functions.


def changecase(func):
    def myinner():
        return func().upper()
    return myinner
    
@changecase
def my_habit():
    return "hello sally"

print(my_habit())
print("--------------------------------------------")


# multiple Decorators:

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreetings(func):
    def myinner():
        return "Hello " + func() +" Have a good day!"
    
    return myinner

@changecase
@addgreetings

def myfunction():
    return "tobi"
print(myfunction())
    

#preventing function Metadata:

def my_kar():
    return "Have a great day"

print(my_kar.__name__)
    
