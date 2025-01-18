from sys import maxsize

number = input()

min_num = maxsize

while number != 'Stop':
    if min_num > int(number):
        min_num = int(number)

    number = input()

print(min_num)