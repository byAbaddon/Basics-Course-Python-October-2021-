birthday_cake = int(input()) * int(input())

while True:
    try:
        pieces = int(input())
        birthday_cake -= int(pieces)
        if birthday_cake <= 0:
            print(f'No more cake left! You need {abs(birthday_cake)} pieces more.')
            break
    except:
        print(f'{birthday_cake} pieces are left.')
        break




'''
10
10
20
20
20
20
21

output: No more cake left! You need 1 pieces more.
'''