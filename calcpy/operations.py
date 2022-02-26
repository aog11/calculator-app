#Module with the operations called by calculator.py

#Addition
def addition(numbers):
    result = 0
    for i in numbers:
        result = i + result
    return round(result,2)

#Substraction
def substraction(numbers):
    
    result = 0
    first_run = 0 #Variable to detect the first run of the loop

    for i in numbers:
        #Assigning the first number of the list to result in order to preserve the sign
        if first_run == 0:
            result = i
            first_run = 1
        else:
            result -= i
    return round(result,2)

#Multiplication
def multiplication(numbers):
    result = 1
    for i in numbers:
        result = result * i
    return round(result,2)

#Division
def division(numbers):

    result = 1
    first_run = 0 #Variable to detect the first run of the loop

    for i in numbers:
        #Skiping if 0 is the first operand
        if first_run == 0 and i == 0:
            result = 0
            first_run = 1
            continue
        elif first_run == 0:
            result = i / result
            first_run = 1
        #Undefined result if 0 appears after the first operand for the division operation
        elif first_run == 1 and i == 0:
            return 'undefined'
        else:
            result/=i
    #Adding more decimals to the result if the result is too close to 0
    if round(result,2) == 0.0:
        return round(result,6)
    else:
        return round(result,2)