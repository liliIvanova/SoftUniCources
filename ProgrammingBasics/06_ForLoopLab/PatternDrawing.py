for num in range(1, 6):
    print(num * '*')

for num in range(4, 0, -1):
    print(num * '*')


########################################
height = int(input('Énter the height of the pyramid:'))

for i in range(1, height + 1):
    print(' ' * (height - i), end='')
    print('*' * (2 * i -  1))

for i in range(1, height + 1):
    print(' ' * (height - i), end='')

    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()