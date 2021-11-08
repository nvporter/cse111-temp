
#current date formula with storing
from datetime import datetime

dateTime = datetime.now()

day= datetime.weekday(dateTime)
#start of tax titles and subtotal calculation
tax = .06

subtotal = float(input('Enter the sub total: '))

salesTaxAmount = subtotal * tax
#seeing what day of the week as to apply the discount
if (day == 1 or day == 2) and subtotal >= 50:
    discount= subtotal * .10
    print(f'Discount amount: {discount:.2f}')


    amount = subtotal - discount

    finTax = amount * tax
    print(f'Sales tax: {finTax:.2f}')

    finTotal = finTax + amount
#if the day doesn't have a discount it'll just do it normally
else:
    finTax = subtotal * tax
    print(f'Sales tax: {finTax:.2f}')

    finTotal = subtotal * tax + subtotal

print(f'Total: {finTotal:.2f}')




