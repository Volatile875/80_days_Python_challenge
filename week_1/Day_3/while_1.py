''' in the while loop first we have to give the condition
then we have to specify the working of function or print statement'''


'''i=1
while i<6:
    print(i)
    i=+1'''

#NOTE= remember to increment i, or else the loop will continue forever.

'''break statement'''


i = 1
while i < 6:
    if i == 3:
        i += 1 # We must increment here too, or we get an infinite loop!
        continue
    print(i)
    i += 1

'''continue statement()'''


i=1
while i>6:
    i+=1
    if i==3:
        continue
    print(i)
    i+=1


#NOTE= the else block will not be executed if the loop is stoped by break Statement.
print("------------------------------------------------------------------------------")
i=1
while i<6:
    if i==4:
        break
    print(i)
    i+=1
else:
    print("i is no longer than 6")


