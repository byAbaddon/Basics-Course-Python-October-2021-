# divisionWithoutRemainder
loop = int(input())
num_list = [int(input()) for _ in range(loop)]
p1 = len(list(filter(lambda el: el % 2 == 0, num_list))) / loop * 100
p2 = len(list(filter(lambda el: el % 3 == 0, num_list))) / loop * 100
p3 = len(list(filter(lambda el: el % 4 == 0, num_list))) / loop * 100
  
print(f'{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%')

'''
3
3
6
9
'''
