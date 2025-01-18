number_of_snowballs = int(input())

best_snowball = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0

for _ in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = (weight / time) ** quality
    if best_snowball < snowball_value:
        best_snowball = snowball_value
        snowball_weight = weight
        snowball_time = time
        snowball_quality = quality

print(f'{snowball_weight} : {snowball_time} = {int(best_snowball)} ({snowball_quality})')