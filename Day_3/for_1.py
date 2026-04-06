# for loop here in python is used fot=r iterating over  asequence like
# (that is either a list, set , tuple, dictonaries, etc.)
#  example are as follows...

fruit={"apple","mango","banana"}
for x in fruit:
    print(x)

###looping through a string:

a="axe"
for x in a:
    if x == a:
        break
    elif 'a' in a:
        print("Yes a is there in the string")
        break
    else:
        print('a is not there')



print("-----------------------------------------------------------")


fruits={"apple","banana","mango"}
for x in fruits:
    if x=="banana":
        continue
    print(x)


print("---------------------------------------------------")

rate={0,1,2,3,4,5,6,7,8,9,10}
for x in range(0, 4):
    print(x)

print("----------------------------------------------------------")


adi=["red","green"]
fruits=['apple','grapes']
for x in adi:
    
    for y in fruits:
        print(x,y)


        