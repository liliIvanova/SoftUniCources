cake_width = int(input())
cake_length = int(input())

pieces = cake_length * cake_width
result = ''

while pieces > 0:
    command = input()

    if command == 'STOP':
        if pieces > 0:
            result = f'{pieces} pieces are left.'
            break
    else:
        taken_pieces = int(command)
        if pieces >= taken_pieces:
            pieces -= taken_pieces
        else:
            result = f'No more cake left! You need {taken_pieces - pieces} pieces more.'
            break

print(result)