ABROAD_ADDITION = 50 / 100
CHARITY_PART = 75 / 100

SUMMER_BULGARIA = 5 / 100
SUMMER_ABROAD = 10 / 100
WINTER_BULGARIA = 8 / 100
WINTER_ABROAD = 15 / 100

dancers_cnt = int(input())
points = float(input())
season = input()
country = input()
reward = 0

if country == 'Bulgaria':

    reward = points * dancers_cnt

    if season == 'summer':
        reward -= reward * SUMMER_BULGARIA

    elif season == 'winter':
        reward -= reward * WINTER_BULGARIA

elif country == 'Abroad':

    reward = points * dancers_cnt
    reward += reward * ABROAD_ADDITION

    if season == 'summer':
        reward -= reward * SUMMER_ABROAD

    elif season == 'winter':
        reward -= reward * WINTER_ABROAD

charity_sum = reward * CHARITY_PART

reward -= charity_sum

print(f'Charity - {charity_sum:.2f}')
print(f'Money per dancer - {reward / dancers_cnt:.2f}')