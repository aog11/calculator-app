#Calculator script
import sys, results

#Initial variables
a = None
b = None

#Taking values sent by a "lazy" Jenkins implementation
if len(sys.argv) > 2:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

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

results.op_result(a, b)