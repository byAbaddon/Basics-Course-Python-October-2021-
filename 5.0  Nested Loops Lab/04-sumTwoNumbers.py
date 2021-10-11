first, second, magic_num = [int(input()) for _ in range(3)]
counter = 0

for i in range(first, second + 1):
    for j in range(first, second + 1):
        counter += 1
        if magic_num == i + j:
            print(f'Combination N:{counter} ({i} + {j} = {magic_num})')
            exit()

print(f'{counter} combinations - neither equals {magic_num}')

'''
1
10
5
'''