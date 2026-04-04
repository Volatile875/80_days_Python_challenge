# Change values in a dictionary:
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964 }
thisdict["year"]=2020
print(thisdict)

#Update method():

thisdict={ 
    "animal":"dog",
    "age":5,
    "colour":"black"
}
thisdict.update({"age":6})
print(thisdict)

#Adding items in a dictionary:
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964 }
thisdict["colour"]="yellow"
print(thisdict)

#pop items():

pratik={
    "name":"pratik",
    "age":22,
    "city":"delhi"
}
pratik.pop("age")
print(pratik)
pratik.popitem()
print(pratik)



#NOTE= The del keyword can also delete the whole dictionary completely.