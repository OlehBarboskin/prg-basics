monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]
food_expense = 0
transport_expense = 0
utilities_expense = 0

for column in monthly_expenses:
    food_expense += column[0]
    transport_expense += column[1]
    utilities_expense += column[2]

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print(f'Food:{food_expense}')
print('Transport:', transport_expense)
print('Utilities:', utilities_expense)
print('Week 1:', monthly_expenses[0])
print('Week 2:', monthly_expenses[1])
print('Week 3:', monthly_expenses[2])
print('Week 4:', monthly_expenses[3])
print('---------------')
print('TOTAL:',sum(monthly_expenses[0]) + sum(monthly_expenses[1]) + sum(monthly_expenses[2]) + sum(monthly_expenses[3]))