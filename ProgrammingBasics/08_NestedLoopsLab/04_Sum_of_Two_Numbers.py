range_low_limit = int(input())
range_high_limit = int(input())
magic_number = int(input())

combinations_ctr = 0
result = ''
combination_found = False

for x in range(range_low_limit, range_high_limit + 1):
    for y in range(range_low_limit, range_high_limit + 1):
        combinations_ctr += 1
        if x + y == magic_number:
            result = f'Combination N:{combinations_ctr} ({x} + {y} = {magic_number})'
            combination_found = True
            break
        else:
            result = f'{combinations_ctr} combinations - neither equals {magic_number}'
    if combination_found == True:
        break

print(result)