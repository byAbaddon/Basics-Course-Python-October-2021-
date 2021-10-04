speed = float(input())
print('slow' if speed <= 10 else 'average' if 10 < speed <= 50 else 'fast' \
    if 50 < speed <= 150 else 'ultra fast' if speed <= 1000 else 'extremely fast')

# 8
# output: slow
