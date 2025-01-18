# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която чете времената на състезателите в секунди,
# въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").

ONE_MIN_IN_SEC = 60

first_time_in_sec = int(input())
second_time_in_sec = int(input())
third_time_in_sec = int(input())

sum = first_time_in_sec + second_time_in_sec + third_time_in_sec

minutes = sum // ONE_MIN_IN_SEC
seconds = sum % ONE_MIN_IN_SEC

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")