# characterSequence
text = input()
sum_num = 0
catalog = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

for i in text:
    if i in catalog:
        sum_num += catalog[i]
print(sum_num)

# hello
