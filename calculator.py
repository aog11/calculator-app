#Calculator script
import sys

#Taking values sent by a "lazy" Jenkins implementation
a = int(sys.argv[1])
b = int(sys.argv[2])

#Addition
def addition(a, b):
    return a + b

#TODO: Substraction

#TODO: Multiplication

#TODO: Division

#Receive the values by input
if a == '':
    print('Please inser the first value: ', end ='')
    a = int(input())

if b == '':
    print('Please inser the second value: ', end ='')
    b = int(input())

result = addition(a,b)
print ('The result is: %s' %(result))