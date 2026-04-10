#clear() method:
thisdict={"name":"pratik",
          "age":22,
          "city":"delhi"}
thisdict.clear()
print(thisdict)

'''del thisdict
print(thisdict)'''

# loops in dictionaries:
 
 
pt={
    "name":"pratik",
    "car":"bmw",
    "age":25
    }
for x in pt:
    print(x)


'''Here you can use single loop to print both keys and values:'''
for x,y in pt.items():
    print(x,y)

#copy() method:
thisdict={
    "name":"pratik",
    "age":22,
    "city":"delhi"
}   
gap=thisdict.copy()
print(gap)

#Nested dictionaries:

my_family={
    "child1":{
        "name":"yash",
        "age":22
    },
    "child2":{
        "name":"pk",
        "age":22
    },
    "child3":{
        "name":"aryan",
        "age":22
    }
}
print(my_family)

print(my_family["child3"])

