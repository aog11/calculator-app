#Calculator script
import sys, os

#Adding current folder to path in order to find the new modules
sys.path.append(os.getcwd() + '/calcpy')

import calcpy

#Receive the amount of opereands by input
print('Please enter the amount of numbers to compute: ', end='')
numbers_amount = calcpy.numbers_validation.validate_operands_number(input())

#Receive the numbers
numbers = []

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