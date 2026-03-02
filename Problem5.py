#Problem5.py
#Project Euler Problem #5

#Name: William Headlee
#Date: 3/2/26
#Assignment: Lab 7
 
"""

My thought process to solve this is, 
if you iterate through every number 
and check if it is divisible by 
all of the intergers up to 20 
you will eventually get to the answer

I made it mildly more efficient by removing 
redudant integers that are checked by others
like how if a number is divisible by 16
it is also divisible by 8, 4, and 2

It also starts at 380 and increments by
380 because 19 * 20 = 380

Printing each number is unnecessary 
but fun to see them tick up 

Also I know there are much more efficient
ways of doing this, but I did it this way
to show I can use multiple functions
even if they are all pretty much the same

"""

def div5(n):
    num = n
    if num % 5 == 0:
        return True
    return False

def div7(n):
    num = n
    if num % 7 == 0:
        return True
    return False

def div9(n):
    num = n
    if num % 9 == 0:
        return True
    return False

def div11(n):
    num = n
    if num % 11 == 0:
        return True
    return False

def div13(n):
    num = n
    if num % 13 == 0:
        return True
    return False

def div16(n):
    num = n
    if num % 16 == 0:
        return True
    return False

def div17(n):
    num = n
    if num % 17 == 0:
        return True
    return False

def div19(n):
    num = n
    if num % 19 == 0:
        return True
    return False

def main():
    num = 380
    while not (div5(num) and div7(num) and div9(num) and div11(num) and div13(num) and div16(num) and div17(num) and div19(num)):
        num += 380
        print(num)
    print("The number divisible by all of the intergers from 1-20 is %d" %num)

main()