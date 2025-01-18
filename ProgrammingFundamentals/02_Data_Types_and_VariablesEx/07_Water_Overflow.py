water_tank = 255

water_sips_number = int(input())
poured_water = 0

for _ in range(water_sips_number):
    water_sip = int(input())

    if water_tank >= poured_water + water_sip:
        poured_water += water_sip
    else:
        print('Insufficient capacity!')
print(poured_water)

