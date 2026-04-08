# **kwargs: If you do not have many keywords arguments will be passed into your function, add two asteriks** before name.
#Inside the function; Kwargs become dictonary.
# example:

def my_fun(**myvar):
    print("Type:",type(myvar))
    print("Name:",myvar["name"])
    print("Age:",myvar["age"])
    print("All Data:",myvar)

ob=my_fun(name="tobi",age=30, city='delhi')


#using the kwargs with regular arguments:

def my_pratik(username,**details):
    print("username:",username)
    print("Additional_details:")
    for key, value in details.items():
        print(" ",key +":",value)

my_pratik("emil123", age=25,)



#Combining both together:

'''1. regular arguments
2. *args
3. **kwargs
'''

def my_func(title,*args,**kwargs):
    print("Titles:",title)
    print("positional arguments:",args)
    print("keywords arguments:",kwargs)
my_func("user_info","rax","max","ganesh",age=25, city="oslo")

#Unpacking Arguments:

#1. Unpacking Lists with * :
# if you stored valurs in the list, you can use * to unpack them>...

def my_alt(a,b,c):
    return a+b+c

number=[1,2,3]
result=my_alt(*number)
print(result)


#2. Unpacking the dictnories with **Kwargs:
# if you have keywords arguments stored in a dict., you can use** to unpack them:


def f_rare(fname,lname):
    print("Hello",fname,lname)
person={"fname":"shruti","lname":"panda"}

f_rare(**person)