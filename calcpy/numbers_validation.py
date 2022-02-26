#Module to validate the numbers received for the amount of operands and the operations

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

#Validate that the recevied value for amount of operands is a whole number
def validate_operands_number(num):
    while True:
        if num.isdigit():
            break
        else:
            print('Please enter a valid whole number: ',end='')
            num = input()
    return int(num)
