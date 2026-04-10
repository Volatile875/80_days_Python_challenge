# by default , a function must be called with the correct number of argument
# however, sometimes you don't know how many argument that will be passed into you functions.
# *args and **kwargs allows the function to have n number of arguments.

# Q. what is *args? *args are hte parameters allow a function to accept the no, of positional arguments,
''' NOte- inside the function, the args become tuples.'''


#ex1

def my_fun(*kids):
    print("the young child " + kids[2])

my_fun("pratik", "yash","vishal")



def prt(*total):
    print("there are "+ total[1]+ " number of students in my class")
prt("23","45","63")


# expample 2: using args with regular argumenrts: you can combine the regular paramenter with args.

def xyz(great, *names):
    for name in names:

        print(great, name)

xyz("hello","jay", "ram","krish")


    
# example practical of *args:

def my_func(*number):
    total=0
    for num in number:
        total+=num
    return total
print(my_func(1,2,3,4))
print(my_func(10,20,30,40))
print(my_func(5))


#: finding the maximum values:

def myfact(*nums):
    if len(nums)==0:
        return None
    max=nums[0]
    for num in nums:
       if num > max:
        max=num
    return max

print(myfact(3,7,8,9))






