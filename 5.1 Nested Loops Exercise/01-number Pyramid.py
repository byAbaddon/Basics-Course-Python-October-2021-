# numberPyramid
num = int(input())
current = 0
result = ''

for r in range(1, num + 1):
    for c in range(0, r):
        current += 1
        result += str(current) + ' '
        if current == num:
            print(result)
            exit()

    print(result)
    result = ''

# 15
