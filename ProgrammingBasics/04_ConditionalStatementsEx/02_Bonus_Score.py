# Дадено е цяло число – начален брой точки.
# Върху него се начисляват бонус точки по правилата, описани по-долу.
# Да се напише програма, която пресмята бонус точките, които получава числото и
# общия брой точки (числото + бонуса).
# •	Ако числото е до 100 включително, бонус точките са 5;
# •	Ако числото е по-голямо от 100 и по-малко или равно на 1000, бонус точките са 20% от числото;
# •	Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
#
# •	Допълнителни бонус точки (начисляват се отделно от предходните):
# o	За четно число  + 1 т.
# o	За число, което завършва на 5  + 2 т.

LIMIT_1 = 100
LIMIT_2 = 1000

BONUS_1 = 5
BONUS_2_PERC = 20/100
BONUS_3_PERC = 10/100

BONUS_EVEN = 1
BONUS_ENDS_5 = 2

start_points = int(input())
bonus_points = 0

if start_points <= LIMIT_1:
    bonus_points = BONUS_1
elif start_points > LIMIT_2:
    bonus_points = start_points * BONUS_3_PERC
else:
    bonus_points = start_points * BONUS_2_PERC

if start_points % 2 == 0:
    bonus_points += 1

if start_points % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(bonus_points + start_points)