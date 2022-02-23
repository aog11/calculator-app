#Module with the operations called by calculator.py

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