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

#Validate that the received value by input is a number
def validate_number (num):
    while True:
        if num.isnumeric() == False:
            print('Please enter a valid number: ', end='')
            num = input()
        else:
            break
    return int(num)

#Receive the values by input
if a is None:
    print('Please insert the first value: ', end ='')
    a = input()
    a = validate_number(a)

if b is None:
    print('Please insert the second value: ', end ='')
    b = input()
    b = validate_number(b)

#Results
result = addition(a,b)
print ('The addition result is: %s' %(result))

result = substraction(a,b)
print ('The substraction result is: %s' %(result))

result = multiplication(a,b)
print ('The multiplication result is: %s' %(result))

result = division(a,b)
print ('The division result is: %s' %(result))