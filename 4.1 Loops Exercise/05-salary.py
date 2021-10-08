# salary
open_tabs, salary = int(input()), int(input())
collection_list = [input() for _ in range(open_tabs)]
fb = len(list(filter(lambda el: el == 'Facebook', collection_list))) * 150
ins = len(list(filter(lambda el: el == 'Instagram', collection_list))) * 100
red = len(list(filter(lambda el: el == 'Reddit', collection_list))) * 50

total = salary - (fb + ins + red)
print(f'You have lost your salary.' if total <= 0 else f'{total}')

'''
3
500
Github.com
Stackoverflow.com
softuni.bg
'''
