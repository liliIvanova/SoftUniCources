P1_LIMIT = 200
P2_LIMIT = 399
P3_LIMIT = 599
P4_LIMIT = 799

numbers_cnt = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

p1_perc = 0
p2_perc = 0
p3_perc = 0
p4_perc = 0
p5_perc = 0


for i in range(numbers_cnt):
    number = int(input())

    if number < P1_LIMIT:
        p1 += 1
    elif P1_LIMIT <= number <= P2_LIMIT:
        p2 += 1
    elif P2_LIMIT < number <= P3_LIMIT:
        p3 += 1
    elif P3_LIMIT < number <= P4_LIMIT:
        p4 += 1
    else:
        p5 += 1

p1_perc = p1/numbers_cnt * 100
p2_perc = p2/numbers_cnt * 100
p3_perc = p3/numbers_cnt * 100
p4_perc = p4/numbers_cnt * 100
p5_perc = p5/numbers_cnt * 100

print(f'{p1_perc:.2f}%')
print(f'{p2_perc:.2f}%')
print(f'{p3_perc:.2f}%')
print(f'{p4_perc:.2f}%')
print(f'{p5_perc:.2f}%')
