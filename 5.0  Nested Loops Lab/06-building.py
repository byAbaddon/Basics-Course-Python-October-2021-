floor = int(input())
rooms = int(input())
arr = []

for i in range(1, floor + 1):
    for j in range(0, rooms):
        if i == floor:
            arr.append(f'L{i}{j}')
            continue
        if (i & 1) == 0:
            arr.append(f'O{i}{j}')
        else:
            arr.append(f'A{i}{j}')

while len(arr) != 0:
    template = ''
    for _ in range(0, rooms):
        template += arr.pop() + ' '

    print(' '.join(reversed(template.split(' '))))

# 6, 4
