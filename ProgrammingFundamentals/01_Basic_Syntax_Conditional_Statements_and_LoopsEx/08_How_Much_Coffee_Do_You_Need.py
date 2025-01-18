command = input()
coffees_number = 0

while command != 'END':

    if command.lower() == 'coding' or command.lower() == 'dog' or command.lower() == 'cat' or command.lower() == 'movie':
        if command.islower():
            coffees_number += 1
        else: # command.isupper()
            coffees_number += 2
    command = input()

if coffees_number > 5:
    print('You need extra sleep')

else:
    print(coffees_number)
