month = int(input('Enter month number (1-12): '))

if month >= 10:
    quarter = 4
elif month >=7:
    quarter = 3
elif month >=4:
    quarter = 2
else: 
    quarter = 1

print (f'The month is in quarter {quarter}')