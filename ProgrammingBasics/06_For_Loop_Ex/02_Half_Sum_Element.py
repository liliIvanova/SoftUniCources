from sys import maxsize

numbers_cnt = int(input())

max_num = -maxsize
sum_num = 0

for i in range(numbers_cnt):
    number = int(input())

    if max_num < number:
        max_num = number

    sum_num += number

if max_num == (sum_num - max_num):
    print(f'Yes\nSum = {max_num}')
else:
    print(f'No\nDiff = {abs(max_num - (sum_num - max_num))}')