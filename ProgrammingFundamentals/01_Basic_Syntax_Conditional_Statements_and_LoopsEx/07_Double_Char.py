str = input()

while str != 'End':

    if str != 'SoftUni':
        doubled_str = ''

        for ch in str:
            doubled_str += ch * 2
        print(doubled_str)

    str = input()

