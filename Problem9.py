#Problem5.py
#Project Euler Problem #9

#Name: William Headlee
#Date: 3/2/26
#Assignment: Lab 7

"""

My thought process:

a^2 + b^2 = c^2

a^2 + b^2 = 1000
a + b + c = 1000

c = 1000 - a + b

So if we say a < b < c
we can use nested for loops 
to try every value of b for
a value of a and then move on
if it doesn't work

Then when you do find the answer
find the product abc as Prob9 specifies

"""

def is_pythagorean(a, b, c):
    """Checks if the three numbers satisfy the Pythagorean theorem"""
    return (a**2 + b**2) == c**2

def calculate_product(a, b, c):
    """Returns the product of the triplet"""
    return a * b * c

def main():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            
            if c > b: # Ensure a < b < c
                if is_pythagorean(a, b, c):
                    result = calculate_product(a, b, c)
                    print("a: %d, b: %d, c: %d" %(a,b,c))
                    print("The product abc is: %d" %result)
                    return

main()