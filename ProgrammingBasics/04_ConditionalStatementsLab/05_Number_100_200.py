# Да се напише програма, която чете цяло число, въведено от потребителя и проверява дали е под 100, между 100 и 200 или над 200. Ако числото е:
# •	под 100 отпечатайте: "Less than 100"
# •	между 100 и 200 отпечатайте: "Between 100 and 200"
# •	над 200 отпечатайте: "Greater than 200"
# Да се напише програма, която чете цяло число, въведено от потребителя и проверява дали е под 100, между 100 и 200 или над 200. Ако числото е:
# •	под 100 отпечатайте: "Less than 100"
# •	между 100 и 200 отпечатайте: "Between 100 and 200"
# •	над 200 отпечатайте: "Greater than 200"

LOWER_LIMIT = 100
UPPER_LIMIT = 200

a = int(input())

if a < LOWER_LIMIT:
    print("Less than 100")
elif a > UPPER_LIMIT:
    print("Greater than 200")
else:
    print("Between 100 and 200")