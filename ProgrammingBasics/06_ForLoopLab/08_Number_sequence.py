from sys import maxsize

number = int(input())

min_num = maxsize
max_num = -maxsize

for _ in range(number):
    current_number = int(input())
    if current_number > max_num:
        max_num = current_number
    if current_number < min_num:
        min_num = current_number

print(f"Max number: {max_num}\nMin number: {min_num}")