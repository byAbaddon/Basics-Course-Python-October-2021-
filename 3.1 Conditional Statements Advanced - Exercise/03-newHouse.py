flowers = input()
count = int(input())
budget = float(input())
result = 0

flowers_price = {
    'Roses': 5,
    'Dahlias': 3.80,
    'Tulips': 2.80,
    'Narcissus': 3,
    'Gladiolus': 2.50,
}

if flowers == 'Roses' and count > 80:
    result = count * 0.90
elif flowers == 'Dahlias' and count > 90:
    result = count * 0.85
elif flowers == 'Tulips' and count > 80:
    result = count * 0.85
elif flowers == 'Narcissus' and count < 120:
    result = count * 1.15
elif flowers == 'Gladiolus' and count < 80:
    result = count * 1.20
else:
    result = count

result *= flowers_price[flowers]
total = budget - result

if total > -1:
    print(f'Hey, you have a great garden with {count} {flowers} and {total:.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(total):.2f} leva more.')

'''
Roses
55
250
'''
