numbers_cnt = int(input())

left_sum = 0
right_sum = 0

for _ in range(numbers_cnt):
    left_sum += int(input())

for _ in range(numbers_cnt):
    right_sum += int(input())


if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')
