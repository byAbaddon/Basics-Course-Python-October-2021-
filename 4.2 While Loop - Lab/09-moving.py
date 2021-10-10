from functools import reduce
free_space = reduce(lambda a, x: a * x, [int(input()) for _ in range(3)])
cubic_mt = 0

while True:
    current_box = input()
    try:
        cubic_mt += int(current_box)
        if free_space < cubic_mt:
            print(f'No more free space! You need {abs(free_space - cubic_mt)} Cubic meters more.')
            break
    except:
        print(f'{(free_space - cubic_mt)} Cubic meters left.')
        break


'''
10
10
2
20
20
20
20
122

output: No more free space! You need 2 Cubic meters more.

---------------------------
10
1
2
4
6
Done

output: 10 Cubic meters left.
'''
