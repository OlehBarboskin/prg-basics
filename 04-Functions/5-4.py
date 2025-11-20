def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Very Good'
    elif points >= 10:
        grade = 'Satisfactory'
    elif points < 10:
        grade = 'Fail'
    return grade

test_grade = 15
final_grade = pts_to_grade(test_grade)
print(f'A student with {test_grade} points has a grade: {pts_to_grade(15)}')