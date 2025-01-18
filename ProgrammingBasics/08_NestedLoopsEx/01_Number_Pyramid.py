n = int(input())
number = 1
end_number_reached = False

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print( str(number) + ' ' ,  end='')

        if number >= n:
            end_number_reached = True
            break

        number += 1

    if end_number_reached == True:
        break
    print()