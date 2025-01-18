from sys import maxsize

number = input()

max_num = -maxsize

while number != 'Stop':
    if max_num < int(number):
        max_num = int(number)

    number = input()

print(max_num)