groups_cnt = int(input())
musala_climbers = 0
montblan_climbers = 0
kilimandjaro_climbers = 0
K2_climbers = 0
everest_climbers = 0
climbers_cnt = 0

for _ in range(groups_cnt):
    num_of_people_in_group = int(input())

    if num_of_people_in_group <= 5:
        musala_climbers += num_of_people_in_group

    elif 6 <= num_of_people_in_group <= 12:
        montblan_climbers += num_of_people_in_group

    elif 13 <= num_of_people_in_group <= 25:
        kilimandjaro_climbers += num_of_people_in_group

    elif 26 <= num_of_people_in_group <= 40:
        K2_climbers += num_of_people_in_group

    else:
        everest_climbers += num_of_people_in_group

climbers_cnt = musala_climbers + montblan_climbers + kilimandjaro_climbers + K2_climbers +everest_climbers

print(f'{musala_climbers/climbers_cnt * 100:.2f}%')
print(f'{montblan_climbers/climbers_cnt * 100:.2f}%')
print(f'{kilimandjaro_climbers/climbers_cnt * 100:.2f}%')
print(f'{K2_climbers/climbers_cnt * 100:.2f}%')
print(f'{everest_climbers/climbers_cnt * 100:.2f}%')