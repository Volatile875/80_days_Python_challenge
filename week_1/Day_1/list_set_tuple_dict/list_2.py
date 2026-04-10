#while loops with lists 
#traversing in liat using while loop;
'''mohit = ["APP","chocolate","icecream","mango","banana"]
i=0
while i<len(mohit):
    print(mohit[i])
    i+=1'''


#list methods:
#adding the elements in list to another list with using append method;
'''thislist = ["apple","banana","cherry"]
[print(x) for x in thislist]


yash=[]
for x in thislist:
    if "a" in x:
         yash.append(x)

print(yash)'''

#list comprehension: and same above code 
fruits=["apple","banana","cherry"]
newlist=[x for x in fruits if "a" in x]
print(newlist)


print("--------------------------------------")


newlist=[x for x in range(10)]
print(newlist)


newlist.sort()
print(newlist)
newlist.sort(reverse=True)
print(newlist)