types, row, col = [input() for _ in range(3)]

projectionType = {'Premiere': 12.0, 'Normal': 7.5, 'Discount': 5.0}
print(f'{(projectionType[types] * int(row) * int(col)):.2f} leva')

'''
Premiere
10
12
'''
