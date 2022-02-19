#Calculator script
import sys

#Initial variables
a = None
b = None

#Taking values sent by a "lazy" Jenkins implementation
if len(sys.argv) > 2:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

#Addition
def addition(a, b):
    return a + b

#Substraction
def substraction(a, b):
    return a - b

#Multiplication
def multiplication(a, b):
    return a * b

#Division
def division(a, b):
    return a / b

#Receive the values by input
if a is None:
    print('Please inser the first value: ', end ='')
    a = int(input())

if b is None:
    print('Please inser the second value: ', end ='')
    b = int(input())

#Results
result = addition(a,b)
print ('The addition result is: %s' %(result))

result = substraction(a,b)
print ('The substraction result is: %s' %(result))

result = multiplication(a,b)
print ('The multiplication result is: %s' %(result))

result = division(a,b)
print ('The division result is: %s' %(result))