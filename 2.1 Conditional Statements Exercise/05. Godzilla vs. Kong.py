budget, statist, clothes = [float(input()) for x in range(3)]
decors = budget / 10
clothes_sum = statist * clothes

if statist > 150:
    clothes_sum *= 0.9

budget -= decors + clothes_sum

if budget >= 0:
    print(f'Action!\nWingard starts filming with {budget:.2f} leva left.')
else:
    print(f'Not enough money!\nWingard needs {abs(budget):.2f} leva more.')

'''
20000
120
55.5
'''
