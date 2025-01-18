CAL_PER_FAT = 9
CAL_PER_PROT = 4
CAL_PER_CARBO = 4

fats_perc = int(input())
proteins_perc = int(input())
carbohydrates_perc = int(input())
total_calories = int(input())
water_perc = int(input())


fat_weight = ((fats_perc / 100) * total_calories)/CAL_PER_FAT
proteins_weight = (proteins_perc / 100 * total_calories) / CAL_PER_PROT
carbohydrates_weight = (carbohydrates_perc / 100 * total_calories) / CAL_PER_CARBO

food_weight = fat_weight  + proteins_weight + carbohydrates_weight
calories_per_gram = total_calories / food_weight

calories_per_gram -= water_perc / 100 * calories_per_gram

print(f'{calories_per_gram:.4f}')



