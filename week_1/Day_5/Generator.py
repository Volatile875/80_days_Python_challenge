# generators function is called, it retuns a generators object, which is an iterator.
# generators are the functions that can puse and resume their execution.
# The code inside the function is not executed yet, it is onlc compiled. The function only executed when you iterates over the generatoe.


def my_gen():
    yield 1
    yield 2
    yield 3
for value in my_gen():
    print(value)

print("----------------------------------------------")

#generator allows you to iterate over data without storing the entire dataset in memory.
#instead usinf return; generator uses the yeild keywords.

# generator can Save memory how??

def large_sequence(n):
    for i in range(n):
        yield i
'''this doesn't create a million number in memory'''

gen= large_sequence(10000)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

"""btw you can mutually iterate througha generator using the next() function."""

# Generator Expression : list comprehension  vs generator expression

list_comp=[x*x for x in range(5)]
print(list_comp)

gen_exp=(x*x for x in range(5))
print(gen_exp)
print(list(gen_exp))


print("----------------------------------------------------------")

#generator Method:
# 1. Send() Method= allows you to send a value to the generator.

def echo_generator():
    while True:
        received = yield 
        print ("received:" , received)
gen=echo_generator()
next(gen)
gen.send("Hello")
gen.send("World")
