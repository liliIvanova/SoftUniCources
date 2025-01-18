# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат
# часове:минути.
# Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

ONE_HOUR_IN_MIN = 60
ONE_DAY_IN_HOURS = 24
TIME_DELTA = 15

hour = int(input())
minutes = int(input()) + TIME_DELTA

if minutes >= ONE_HOUR_IN_MIN:
    hour += (minutes // ONE_HOUR_IN_MIN)
    minutes -= ONE_HOUR_IN_MIN

if hour >= ONE_DAY_IN_HOURS:
    hour -= ((hour//ONE_DAY_IN_HOURS) * ONE_DAY_IN_HOURS)

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
