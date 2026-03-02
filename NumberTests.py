#NumberTests.py
#Name: William Headlee
#Date: 3/2/26
#Assignment: Lab 7

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False
  
def findDivisors(n, d):
  """Returns list of divisors for n based on the root"""
  num = n
  divisors = d
  root = int(num ** 0.5)
  for i in range(root):
    divisors.append(i + 2)
  return divisors

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  num = p
  divisors = []

  if num <= 1:
    return False
  
  if isEven(num):
    return False
  
  
  divisors = findDivisors(num, divisors)

  for i in divisors:
    if num % i == 0:
      return False
    
  return True

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]

  num = int(input("Enter a number: "))

  if isPrime(num):
    print("%d is a prime number" %(num))

  elif isEven(num):
    print("%d is an even number" %(num))
  
  else:
    print("%d is not a prime number" %(num))


if __name__ == '__main__':
    main()
