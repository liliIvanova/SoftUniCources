MAX_CHANGE = 2.99

coins_cnt = 0
rest_sum = 0

change = int(float(input() ) * 100)

while change - 200 >= 0:
    coins_cnt += 1
    change -= 200

while change >= 100:
    coins_cnt += 1
    change -= 100

while change >= 50:
    coins_cnt += 1
    change -= 50

while change >= 20:
    coins_cnt += 1
    change -= 20

while change >= 10:
    coins_cnt += 1
    change -= 10

while change >= 5:
    coins_cnt += 1
    change -= 5

while change >= 2:
    coins_cnt += 1
    change -= 2

while change >= 1:
    coins_cnt += 1
    change -= 1


print(coins_cnt)