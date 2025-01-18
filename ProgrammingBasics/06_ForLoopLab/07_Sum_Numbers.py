numbers_cnt = int(input())

sum_of_numbers = 0
current_num = 0

for _ in range(numbers_cnt):
    current_num = int(input())
    sum_of_numbers += current_num

print(sum_of_numbers)