# # a lambda is a small anonymous function.
# # lambda function can take any number of arguments, but can only have on expression.
# # Syntax:
# # lambda arguments:expression

# x= lambda a:a+10
# print(x(5))

# x=lambda a,b: a*b
# print(x(5,6))

# x=lambda a,b,c:a+b+c
# print(x(4,5,6))


#Q. Why do we use lambda function?
# the power of lambda is better shown when you use them as an anynomous function inside another function.
 

# def my(n=0):
#     return lambda m,a,b:m+n+a+b
# mydouble=my()
# print(mydouble)

# # print(mydouble(11,1,2))
# a=input().split()
# print(type(a),type(a[0]))
# print(a)

# b=list(map(int,input().split("\n")))
# print(type(b),type(b[0]))
# b.sort(reverse=True)
# print(b)

# we can use lambda function with built in functions : the functions are map(), filter(), sorted()

#map()


# number=[1,2,3,4,5,6,7,8,9]
# double =list(map(lambda x:x**2,number))
# print(double)


# #filter()

# no=[9,8,7,5,6,2,3]
# odd_on=list(filter(lambda x:x%2!=0,no))
# print(odd_on)


# #sorted()

std=[("yash",25),("max",39),("linus",34)]
sorted_std=sorted(std, key=lambda x:x[1], reverse=True)
print(sorted_std)


b = sorted(map(int, input().split()), reverse=True)


print(type(b), type(b[0]))
print(b)

print(help(sorted))