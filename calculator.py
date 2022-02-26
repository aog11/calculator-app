#Calculator script
import sys, os, random
from getpass import getuser

#Adding current folder to path in order to find the new modules
sys.path.append(os.getcwd() + '/calcpy')

import calcpy


#List with the numbers to operate on
numbers = []

#Random numbers for testing of Jenkins pipeline
if getuser == 'jenkins':
    numbers_amount = random.randint(1, 10)

    for i in range(numbers_amount):
        numbers.append(random.randrange(-10,10))

#Receive the numbers when script is called by a user
if len(numbers) == 0:

    #Receive the amount of operands by input
    print('Please enter the amount of numbers to compute: ', end='')
    numbers_amount = calcpy.numbers_validation.validate_operands_number(input())

    for i in range(numbers_amount):
        
        #Printing a differrent message based on the loop
        if i == 0:
            print('Please enter the first number: ', end='')
        elif i == numbers_amount - 1:
            print('Please enter the final number: ', end='')
        else:
            print('Please enter the next number: ', end='')
        
        #Receiving the number
        numbers.append(calcpy.numbers_validation.validate_number(input()))

calcpy.results.op_result(numbers)