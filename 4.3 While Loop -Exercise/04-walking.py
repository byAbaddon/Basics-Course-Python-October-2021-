steps = 10000
while steps > 0:
    el = input()
    if el != 'Going home':
        steps -= int(el)
    else:
        steps -= int(input())
        if steps > 0:
            print(f'{abs(steps)} more steps to reach goal.')
            exit()
print(f'Goal reached! Good job!\n{abs(steps)} steps over the goal!')

'''
1000
1500
2000
6500
'''

