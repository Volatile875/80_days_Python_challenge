#  Sets are used to store multiple items in a single variable.
#  A set is a collection which is unordered, unchangeable, and unindexed.
#  In Python sets are written with curly brackets.


#using set as a constructor:

thisset= set(("apple","banana","cherry"))
print(thisset)

thisset={"apple","banana","cherry"}
print("apple" in thisset)


#adding and updating the elements in the set using add() method:
thisset={1,2,23,45,67}
thisset.add(89)
print(thisset)

'''x={1,2,3,4,5}
y={6,7,8,9,10}
x.update(y)
print(x)'''

arr=[9,8,7,6]
x={1,2,3}
y={4,5,6}
x.update(y)
print(x)


# remove() and discard() the elements in the set using remove() method:

thisset={"apple","banana","cherry"}
thisset.remove("apple")
print(thisset)


thisset.discard("banana")
print(thisset)


#exception in removing the element is pop() methosd():
thisset={"apple","banana","cherry"}
thisset.pop()
print(thisset)