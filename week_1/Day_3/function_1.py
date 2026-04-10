# a function is a block of code which olnly runs when it is called
# A function can return data as a result.
# A function helps avoding repetations.


def my_fun():
    print ("hello")

my_fun()


'''converting fah to celcius '''


def fah_to_cel(feh):
    return (feh-32)*5/9

print(fah_to_cel(77))


# if a function doesn't have a return statement it returns None by default.

#1 Arguments function = information can be passed intofunctions as agruments. arguments are specified
#after the function, add as many as you want just need to separate by comma.


'example'

def my_fv(name):
    print('Welcome '+ name)

my_fv("Pratik")

# 1. default parameter Values: you can assign default values to parameters, if the a function is called without any argument
#----  then it is called default values. example are as follows.

def my_prt(name="friend"):
    print("hello world",name)
my_prt("yesh")
my_prt()
my_prt("pratik")

## 2. You can send argument with the key=value syntax.

def my_flex(animal, name):
    print("I have a", animal)
    print("My", animal +"s name is ", name)

my_flex(animal="dog", name="buddy")

# the Phase keyword arguments is often shortend to kwargs in python documentation.

'''Positional Argumnets
when a call a function with arguments without using keywords, they are called as positional arguments. 
But positional arguments must be in the correct orders.'''

def my_using(name,animal):
    print("I have a", animal)
    print("My",animal + "name is", name)

my_using("alex","dog")    

# Mixing Positional and Keyword Aruguments :

def my_pack(animal, name, age):
    print (f"I have a", age,"year old", animal, "named as",name)

my_pack(animal="lion",name='fester',age=20)

