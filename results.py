#Module with the result of the operations

import operations

#Results
def op_result (a, b):
    print('\nWith the received values {0} and {1}, the results are:\n'.format(a, b))

    result = operations.addition(a,b)
    print ('The addition result is: %s' %(result))

    result = operations.substraction(a,b)
    print ('The substraction result is: %s' %(result))

    result = operations.multiplication(a,b)
    print ('The multiplication result is: %s' %(result))

    result = operations.division(a,b)
    print ('The division result is: %s' %(result))