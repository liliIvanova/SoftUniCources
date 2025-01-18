number = int(input())


for i in range(1111, 10_000):
    for digit in str(i):

        if digit == '0':
            break

        if number % int(digit) != 0:
            break
    else:
        print(i, end=' ')

