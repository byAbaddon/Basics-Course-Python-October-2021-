name = input()
grade = 0
count = 0
attempt = False

while count < 12:
    current = float(input())
    if current >= 4.0:
        grade += current
        count += 1
    else:
        if attempt:
            print(f'{name} has been excluded at {count + 1} grade')
            exit()
        attempt = True

print(f'{name} graduated. Average grade: {grade / 12 :.2f}')

'''
Gosho
5
5.5
6
5.43
5.5
6
5.55
5
6
6
5.43
5

output: Gosho graduated. Average grade: 5.53
-------------
Mimi
5
6
5
6
5
6
6
2
3

output: Mimi has been excluded at 8 grade
'''