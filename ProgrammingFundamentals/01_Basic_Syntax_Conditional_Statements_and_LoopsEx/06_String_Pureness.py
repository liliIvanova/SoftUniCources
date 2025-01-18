number_of_strings = int(input())

for _ in range(number_of_strings):
    current_str = input()

    if ',' in current_str or '.' in current_str or '_' in current_str:
        print(f'{current_str} is not pure!')
    else:
        print(f'{current_str} is pure.')