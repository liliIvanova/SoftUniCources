book_name = input()
books_ctr = 0

while True:
    next_book = input()

    if next_book == book_name:
        print(f'You checked {books_ctr} books and found it.')
        break

    elif next_book == 'No More Books':
        print(f'The book you search is not here!\nYou checked {books_ctr} books.')
        break

    books_ctr += 1