#Module with the result of the operations

import operations

#Results
def op_result (numbers):
    print('\nWith the received values {0}, the results are:\n'.format(numbers))

    result = operations.addition(numbers)
    print ('The addition result is: %s' %(result))

    result = operations.substraction(numbers)
    print ('The substraction result is: %s' %(result))

    result = operations.multiplication(numbers)
    print ('The multiplication result is: %s' %(result))

    result = operations.division(numbers)
    print ('The division result is: %s' %(result))