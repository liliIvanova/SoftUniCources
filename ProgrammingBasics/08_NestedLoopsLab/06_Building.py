floors = int(input())
rooms = int(input())
fl_name =''

for fl in range(floors, 0, -1):
    for r in range(0, rooms):
        if fl != floors:
            if fl % 2 == 0: # even floors
                fl_name = f'O{fl}{r}'

            else: # odd floors
                fl_name = f'A{fl}{r}'

        else:
            fl_name = f'L{fl}{r}'

        print(fl_name, end=' ')

    print()