import  math

KM_TARGET = 1000

number_of_training_days = int(input())
first_day_kms = float(input())

total_kms = first_day_kms
norm_increase_kms = first_day_kms

for _ in range(number_of_training_days):

    norm_increase = int(input())

    norm_increase_kms += norm_increase / 100 * norm_increase_kms
    total_kms += norm_increase_kms

if total_kms >= KM_TARGET:

    print(f'You\'ve done a great job running {math.ceil(total_kms - KM_TARGET)} more kilometers!')

else:

    print(f'Sorry Mrs. Ivanova, you need to run {math.ceil(KM_TARGET - total_kms)} more kilometers')