decorations_count = int(input())
days_to_christmas = int(input())

ORNAMENT_PRICE = 2
TREE_SKIRT_PRICE = 5
GARLAND_PRICE = 3
LIGHTS_PRICE = 15

ORNAMENT_POINTS = 5
TREE_SKIRT_POINTS = 3
GARLAND_POINTS = 10
LIGHTS_POINTS = 17

money_spent = 0
christmas_spirit = 0

for day in range(1, days_to_christmas + 1):

    if day % 11 == 0:
        decorations_count += 2
    if day % 2 == 0:
        money_spent += ORNAMENT_PRICE * decorations_count
        christmas_spirit += ORNAMENT_POINTS
    if day % 3 == 0:
        money_spent += (TREE_SKIRT_PRICE + GARLAND_PRICE) * decorations_count
        christmas_spirit += TREE_SKIRT_POINTS + GARLAND_POINTS
    if day % 5 == 0:
        money_spent += LIGHTS_PRICE * decorations_count
        christmas_spirit += LIGHTS_POINTS
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        money_spent += TREE_SKIRT_PRICE + GARLAND_PRICE + LIGHTS_PRICE

if days_to_christmas % 10 == 0:
    christmas_spirit -=30
print(f'Total cost: {money_spent}')
print(f'Total spirit: {christmas_spirit}')
