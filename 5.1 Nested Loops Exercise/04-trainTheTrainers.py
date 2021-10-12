# trainTheTrainers
jury_count = int(input())
studentGrade = allStudentGrade = iteration = 0
presentation = input()

while presentation != 'Finish':
    for _ in range(0, jury_count):
        if len(presentation) > 3:
            studentGrade += float(input())
            iteration += 1
            continue
    allStudentGrade += studentGrade
    print(f'{presentation} - {(studentGrade / jury_count):.2f}.')
    studentGrade = 0

    presentation = input()

print(f"Student's final assessment is {(allStudentGrade / iteration):.2f}.")

# 2, While-Loop, 6.00, 5.50, For-Loop, 5.84, '5.66, Finish
