list=["apple","Mango","banana","melon"]
#print(list)

print(list[2:])

print(len(list))
if 3 in list:
    print("yes")
else:    print("no")

list.append("grapes")
print(list)

list.insert(2,"orange")
print(list)

list[4]="kiwi"
print(list)

list[1:3]=["papaya","guava"]
print(list)


list[2:3]=["watermelon","strawberry"]
print(list)

list.remove("watermelon")
print(list)

list.extend(["peach","pear"])
print(list)

list.remove("papaya")
list.remove("strawberry")
list.remove("kiwi")
list.remove("peach")
print(list)


text=[1,2,3,4,5]
text.remove(3)
print(text)


thislist=[1,2,3,4,5]
for x in list:
    print(len(thislist))


for i in range(len(thislist)):
    print(thislist[i])
