student, standard, kid = 0, 0, 0
movie = input()

while movie != "Finish":
    seats = int(input())
    tickets = 0

    for _ in range(0, seats):
        chairs = input()
        if chairs == "End":
            break
        if chairs == 'student':
            student += 1
        if chairs == 'standard':
            standard += 1
        if chairs == 'kid':
            kid += 1
        tickets += 1

    print(f'{movie} - {(tickets / seats * 100):.2f}% full.')
    movie = input()

total_tickets = student + standard + kid
print('Total tickets:', total_tickets)
print(f'{(student / total_tickets * 100):.2f}% student tickets.')
print(f'{(standard / total_tickets * 100):.2f}% standard tickets.')
print(f'{(kid / total_tickets * 100):.2f}% kids tickets.')

'''
The Matrix
20
student
standard
kid
kid
student
student
standard
student
End
The Green Mile
17
student
standard
standard
student
standard
student
End
Amadeus
3
standard
standard
standard
Finish
           '''
