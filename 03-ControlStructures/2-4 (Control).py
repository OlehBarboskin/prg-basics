###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int (input ('number 1:'))
number2 = int (input ('number 2:'))
operator = input ('expression')
if operator == '+':
    calculation = number1 + number2
elif operator == '-':
    calculation = number1 - number2
elif operator == '*':
    calculation = number1 * number2
elif operator == '/':
    calculation = number1 / number2
print (f'{calculation}')