CODE_LIMIT_ID = 88
CODE_GREET_ID = 86

CHAT_CODE_LIMIT_TEXT        = 'Hello'
CHAT_CODE_GREET_TEXT        = 'How are you?'
CHAT_CODE_BELOW_LIMIT_TEXT  = 'GREAT!'
CHAT_CODE_ABOVE_LIMIT_TEXT  = 'Bye.'

n = int(input())

for _ in range(n):
    code = int(input())

    if code < CODE_LIMIT_ID:

        if code == CODE_GREET_ID:
            print(f'{CHAT_CODE_GREET_TEXT}')
        else:
            print(f'{CHAT_CODE_BELOW_LIMIT_TEXT}')
    elif code == CODE_LIMIT_ID:
        print(f'{CHAT_CODE_LIMIT_TEXT}')

    else:
        print(f'{CHAT_CODE_ABOVE_LIMIT_TEXT}')
