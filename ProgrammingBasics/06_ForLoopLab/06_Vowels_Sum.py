A_VALUE = 1
E_VALUE = 2
I_VALUE = 3
O_VALUE = 4
U_VALUE = 5

text = input()
sum = 0

for letter in text:
    if letter == "a":
        sum += A_VALUE
    elif letter == "e":
        sum += E_VALUE
    elif letter == "i":
        sum += I_VALUE
    elif letter == "o":
        sum += O_VALUE
    elif letter == "u":
        sum += U_VALUE

print(sum)