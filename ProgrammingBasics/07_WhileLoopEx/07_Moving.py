width = int(input())
length = int(input())
height = int(input())

volume = length * width * height
result = ''

while volume > 0:
    command = input()

    if command == 'Done':
        if volume > 0:
            result = f'{volume} Cubic meters left.'
            break
    else:
        boxes = int(command)
        if volume >= boxes:
            volume -= boxes
        else:
            result = f'No more free space! You need {boxes - volume} Cubic meters more.'
            break

print(result)