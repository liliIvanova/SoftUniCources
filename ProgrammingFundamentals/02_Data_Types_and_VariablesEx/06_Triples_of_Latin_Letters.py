number_of_letters = int(input())
first_letter = ord('a')
for i in range(first_letter, first_letter + number_of_letters):
    for j in range(first_letter, first_letter + number_of_letters):
        for k in range(first_letter, first_letter + number_of_letters):
            print(chr(i)+chr(j)+chr(k))
