# Tuples are used to store multiple items in a single variable.
# A tuple is a immutable, ordered and also allows duplicate elements.

thistuple=("apple","banana","cherry")
print(len(thistuple))


tuple1=("apple","banana","cherry")
print(type(tuple1))


thistuple=("apple","banana","cherry","apple","cherry")
#using tuples as a constructor()
print(thistuple)
#indexinog in tuples:
tupl3=(("apple","banana","cherry"))
print(tupl3[2:4])
print(tupl3[-2])


imp=("apple","banana","cherry","orange","kiwi","melon","mango")
print(imp[-4:-1])


#checking a particular item in tuple:

if "cherry" in imp:
    print("yes, 'cherry' is in the tuple")

##adding an item in utple by converting it into a list:
x=("apple","banana","cherry")
y=list(x)
y.append("orange")
print(y)
x=tuple(y)
print(x)

print("---------------------------------------")


#adding tuple to tuple:
tuple1=(1,2,3,4,5,6)
tuple2=(7,8,9)
tuple3=tuple1+tuple2
print(tuple3)
#or

tuple1=(1,2,3,4,5,6)
y=("orange",)
print(tuple1+y)

#deleting the tuple:
tuple1=(1,2,3,4,5,6)
del tuple1


#Tuples unpacking ka matlab hai ke ap tuple ke iteams ko variables me alag alag store karna:

fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

#loops in tuples:
thistuple=("apple","banana","cherry")
for x in thistuple:
    print(x,end=" ")


#multipling tuples using * operator:
fruits=("apple","banana","cherry")
mytuple=fruits*2
print(mytuple)

#tuplesmethods:
#count() index() methods are used in tuples:

thistuple=(1,2,3,4,5,6,7,8,9,10)
print(thistuple.count(5))

x=thistuple.index(5)
print(x)






