# equalSumsEvenOddPosition
num_one, num_two = int(input()), int(input())
collection_list = []

for index in range(num_one, num_two + 1):
    get_list = list(map(int, str(index)))
    even = sum(get_list[0::2])
    odd = sum(get_list[1::2])
    if even == odd:
        collection_list.append(index)

print(' '.join(list(map(str, collection_list))))
