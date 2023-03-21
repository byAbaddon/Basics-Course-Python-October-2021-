n = int(input())
print('invalid' if not 100 <= n <= 200 and n != 0 else '')

# -----------------------------------(2)-----------------------------

n = float(input())
print('invalid' if not (100 <= n and not n > 200 or n == 0) else '')

