
basic_salary = 5000
total_salary = 0
is_bonus = True # does the employee receive a bonus
bonus = 1.15 # 15%
value = input('Do you want a Bonus? Y/N:')
if value == 'Y':
    total_salary = basic_salary * bonus
else:
   total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Total salary: {total_salary}')