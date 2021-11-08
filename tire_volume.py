from datetime import datetime

current_date_and_time = datetime.now()

print(f' The current date is: {current_date_and_time:%Y-%m-%d}')

import math


w = float(input('Enter the width of the tire in millimeters: '))

a = float(input('What is the aspect ratio of the tire?: '))

d = float(input('What is the diameter of the wheel in inches?: '))


volume = (math.pi * w**2 * a *(w * a + 2540 * d))/10000000000
print()
print()
if volume > 25:
    price = 126
    print(f'{price} dollars will be the cost of the tire')
else:
    price1 = 96 
    print(f'{price1} dollars will be the cost of the tire') 

print(f'The volume of the tire with a width of {w} millimeters,  aspect ratio of {a}, and a diameter of {d} inches is {volume:.2f} liters')

with open('dimensions.txt', 'at') as dimens_file:

    print(f'{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}', file=dimens_file)

answer = input('Would you like to purchase the tire? yes/no: ')
if answer == 'yes':
    print(f'Your total is {price} dollars')
if answer == 'no':
    print(f'Your total is {price1} dollars ')