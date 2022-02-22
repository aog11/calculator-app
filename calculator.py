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
    return round(a + b, 2)

#Substraction
def substraction(a, b):
    return round(a - b, 2)

#Multiplication
def multiplication(a, b):
    return round(a * b, 2)

#Division
def division(a, b):
    if b == 0:
        return 'undefined'
    else:
        return round(a / b, 2)

#Validate that the received value by input is a number
def validate_number (num):
    while True:
        try:
            float(num)
            break
        except ValueError as v:
            print('Please enter a valid number: ', end='')
            num = input()
    return float(num)

#Results
def results (a, b):
    print('\nWith the received values {0} and {1}, the results are:\n'.format(a, b))

    result = addition(a,b)
    print ('The addition result is: %s' %(result))

    result = substraction(a,b)
    print ('The substraction result is: %s' %(result))

    result = multiplication(a,b)
    print ('The multiplication result is: %s' %(result))

    result = division(a,b)
    print ('The division result is: %s' %(result))

#Receive the values by input
if a is None:
    print('Please insert the first value: ', end ='')
    a = input()
    a = validate_number(a)

if b is None:
    print('Please insert the second value: ', end ='')
    b = input()
    b = validate_number(b)

#Flipping the operands, only when called by the shell ir order to protect my Jenkins test
if len(sys.argv) <= 2:
    
    print('\nWould you like to flip the operands? (y/n): ', end='')
    response = input()

    while True:
        if response.lower() not in ('y','n'):
            print('Please enter a valid option: ', end='')
            response = input().lower()
        elif response == 'y':
            a, b = b, a
            break
        elif response == 'n':
            break

results(a, b)