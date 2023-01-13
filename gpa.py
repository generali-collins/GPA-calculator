numClass = eval(input('\nEnter number of classes taken:  '))
overGrade=0
course_dict={'Course':'Grade'}
for i in range(1,numClass+1):
    className = input(f'Enter the name of Class {i}:  ')
    grade = eval(input(f'Enter your grade for {className}: '))
    course_dict[className]=grade
    overGrade=overGrade+grade
overallGPA = overGrade/numClass
course_dict['Overall GPA']=overallGPA
for key,value in course_dict.items():
    print()
    print(f'{key:<20}{value:>10}\n')
