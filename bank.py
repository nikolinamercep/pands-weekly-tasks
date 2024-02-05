# bank.py
# This program asks you to input two amounts in cents, adds them up and gives you the sum in euros
# Author: Nikolina
number1 = int(input('Please enter amount 1 (in cent): '))
number2 = int(input('Please enter amount 2 (in cent): '))
x = number1 + number2
y = x * 0.01
print ("The sum of these is","\u20ac",y)