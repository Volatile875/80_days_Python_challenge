# when a function calls itself againa and again.
# this has a beneift of meaning that you can loop through data to reacha result.

#example a simple recursion function that counts down from 5:

from typing import Sequence


def countdown(n):
    if n<=0:
        return None
    else:
        print(n)
        countdown(n-1)
countdown(5)

# Base Case and Recursion Case:
# every recursive function must have two part:
# A base case: a condition that stop the recursion
# A recursion case: the function calling itself with a modified arguments.
'''NOTE: without a base case, the function would be calling itself forever, causing a stack overflow.'''

def factorial(n):
    #Base case
    if n==1 or n==0:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))

#Q. Fibonnaci Sequence: where each number is the sum of the two preceding ones. The sequence starts with 0 and 1..........0,1,1,2,3,5,8,13....
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+(fibo(n-2))
    
print(fibo(7))

#Q. Calculate the sun of all elements in the list?
print("---------------------------------------------------")
def sum_list(number):
    if len(number)==0:
        return 0
    else:
        return number[0]+sum_list(number[1:])
my_list=[9,5,6,4,2,3]
print(sum_list(my_list))

    
print("----------------------------------------------------")

#Q. Find the maximum value in the list?

def max(no):
    if len(no)==1:
        return no[0]
    else:
        max_of_rest=max(no[1:])
        return no[0] if no[0]>max_of_rest else max_of_rest
my_list=[3,4,5,7,9,6]
print(max(my_list))