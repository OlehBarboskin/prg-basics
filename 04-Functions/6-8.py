first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord (last)
number_of_letters = ord([first_letter_code:last_letter_code])
print(f'Between {first} and {last} is {number_of_letters} letters')