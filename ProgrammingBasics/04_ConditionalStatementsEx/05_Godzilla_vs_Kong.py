# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
# дали предвидените средства са достатъчни за снимането на филма. За снимките  ще бъдат нужни определен брой
# статисти, облекло за всеки един статист и декор.
# Известно е, че:
# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
# Изход
# На конзолата трябва да се отпечатат два реда:
# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
# •	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.


DECOR_PERC = 10/100
STATISTS_DISC = 10/100
STATISTS_DISC_CNT = 150

budget = float(input())
statists_cnt = int(input())
clothes_per_one = float(input())

decor = budget * DECOR_PERC
clothes = statists_cnt * clothes_per_one

if statists_cnt > STATISTS_DISC_CNT:
    clothes -= clothes * STATISTS_DISC

expences = decor + clothes

if expences > budget:
    print("Not enough money!")
    print(f"Wingard needs {expences-budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget-expences:.2f} leva left.")