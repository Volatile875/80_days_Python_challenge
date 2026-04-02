#Customize sort function():
newlist=[100,50,65,82,23]
def myfunc():
    for x in newlist:

        return abs(x-50)
    newlist.sort(key=myfunc)

ob1=myfunc()
print(ob1)



'''def mylev():
    return abs(thislist[0]-50)

thislist=[100,56,34,56,23,58,78,90]
thislist.sort(key=mylev)
print(mylev())'''


# The function now accepts 'n', which represents each number in the list
def mylev(n):
    return abs(n - 50)

thislist = [100, 56, 34, 56, 23, 58, 78, 90]

# Sorts the list based on which number is closest to 50
thislist.sort(key=mylev)

print(thislist)



#Sort in case sensitive manner:
#by default sort () method is case senesitive,

rev=["banana","Orange","Kiwi","cherry"]
rev.reverse()
print(rev)

print("---------------------------------------")


#list copy method():

prt=["apple","banana","cherry"]
mypt=prt.copy()
print(mypt)

print("---------------------------------------")


#slicing list():

fet=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(fet[2:5])


print(fet[0:3])

print("--------------------------------------")

#Joining the two lists:
list1=["a","b","c"]
list2=[1,2,3]
list3=list1 + list2
print(list3)


print("--------------------------------------")




