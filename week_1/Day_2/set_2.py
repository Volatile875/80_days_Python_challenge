#Sets join() and split() methods:

set1={"apple","banana","cherry"}
set2={1,2,34}
set3=set1.union(set2)
print(set3)


#using "|" as an union operator:
set1={"apple","banana","cherry"}
set2={1,2,34}
set3=set1|set2
print(set3)


#intersection of sets:
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1.intersection(set2)
print(set3)
set3=set1&set2
print(set3)


a=set('hello')
b=set('harsh')
print(a-b)

#symmmetrin difference of sets:

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1.symmetric_difference(set2)
print(set3)

# Set comperihension:

thisset={x for x in "banana" if x!="a"}
print(thisset)


#Python frozen sets:

x=frozenset({"apple","banana","cherry"})
print(type(x))


#python shallow copy:
thisset={"apple","banana","cherry"}
myset=thisset.copy()
print(myset)

