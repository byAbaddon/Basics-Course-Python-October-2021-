def figures(*args):
    if figure == 'square':
        result = args[0] ** 2
    elif figure == 'circle':
        result = args[0] ** 2 * 3.14159
    elif figure == 'rectangle':
        result = args[0][0] * args[0][1]
    else:
        result = args[0][0] * args[0][1] / 2

    return f'{result:.3f}'


figure = input()
if figure == 'square' or figure == 'circle':
    print(figures(float(input())))
else:
    print(figures([float(input()) for _ in range(2)]))


'''
square
5
------
circle
6
--------------
triangle
4.5
20
--------------
rectangle
7
2.5
'''
