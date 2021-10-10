total_sum = 0

while True:
    try:
        current_sum = float(input())
        if current_sum > 0:
            total_sum += current_sum
            print(f'Increase: {current_sum:.2f}')
        else:
            print(f'Invalid operation!\nTotal:', f'{total_sum:.2f}')
            break
    except:
        print('Total:', f'{total_sum:.2f}')
        exit()

# -------------------------------- second solution
# money = 0
# while True:
#     current = input()
#     if current == 'NoMoreMoney':
#         break
#     elif float(current) < 0:
#         print('Invalid operation!')
#         break
#     else:
#         money += float(current)
#         print(f'Increase: {float(current):.2f}')
#
# print(f'Total: {money:.2f}')

'''
5.51
69.42
100
NoMoreMoney
'''
