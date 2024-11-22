test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]
# calculates the number of test questions
question_number = len(test_results)
print (question_number)

# calculates the number of correct answers
correct_answer = 0
incorrect_answer = 0
for answer in test_results:
   if answer is True:
      correct_answer = (correct_answer + 1)
   else:
      incorrect_answer = (incorrect_answer) + 1

print (f'Correct {correct_answer}')
print (f'Incorrect {incorrect_answer}')
percenage = correct_answer * 100 / question_number
print (percenage)