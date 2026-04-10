#dictonaries are used to store values in key value pairs
#they are ordered, changeable and do not allow duplicates

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964            
}
print(type(thisdict))

#dict()Constructor:

this_dict=dict({"brand":"ford","model":"mustang","year":1964})
print(this_dict)


#get keys:

thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964 }
x=thisdict.keys()
print(x)

#get values:
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964 }  
y=thisdict.values()
print(y)