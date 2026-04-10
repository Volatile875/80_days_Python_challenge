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