# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони.
# Има три вида прожекции с билети на различни цени:
# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа), въведени от потребителя,
# и изчислява общите приходи от билети при пълна зала. Резултатът да се отпечата във формат 2 знака след десетичната точка.
# # a

PREIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

proj_type = input()
rows = int(input())
columns = int(input())

seats = rows * columns
incomes = 0

if proj_type == "Premiere":
    incomes = seats * PREIERE
elif proj_type == "Normal":
    incomes = seats * NORMAL
elif proj_type == "Discount":
    incomes = seats * DISCOUNT

print(f"{incomes:.2f}")