# Да се напише програма, която чете скорост (реално число), въведена от потребителя и отпечатва информация за скоростта.
# •	При скорост до 10 (включително) отпечатайте "slow"
# •	При скорост над 10 и до 50 (включително) отпечатайте "average"
# •	При скорост над 50 и до 150 (включително) отпечатайте "fast"
# •	При скорост над 150 и до 1000 (включително) отпечатайте "ultra fast"
# •	При по-висока скорост отпечатайте "extremely fast"

SPEED_LIMIT_1 = 10
SPEED_LIMIT_2 = 50
SPEED_LIMIT_3 = 150
SPEED_LIMIT_4 = 1000

speed = float(input())

if speed <= SPEED_LIMIT_1:
    print("slow")
elif SPEED_LIMIT_1  < speed <= SPEED_LIMIT_2:
    print("average")
elif SPEED_LIMIT_2 < speed <= SPEED_LIMIT_3:
    print("fast")
elif SPEED_LIMIT_3 < speed <= SPEED_LIMIT_4:
    print("ultra fast")
else:
    print("extremely fast")