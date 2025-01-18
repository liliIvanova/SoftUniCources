total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
tickets_per_movie = 0

while True:
    movie_name = input()

    if movie_name == 'Finish':
        print(f'Total tickets: {total_tickets}')
        print(f'{student_tickets * 100 / total_tickets:.2f}% student tickets.')
        print(f'{standard_tickets * 100 / total_tickets:.2f}% standard tickets.')
        print(f'{kids_tickets * 100 / total_tickets:.2f}% kids tickets.')
        break

    free_seats = int(input())
    tickets_per_movie = 0

    while (free_seats - tickets_per_movie) > 0:
        ticket_type = input()

        if ticket_type == 'End':
            break

        tickets_per_movie += 1

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1

    print(f'{movie_name} - {tickets_per_movie * 100 / free_seats:.2f}% full.')
    total_tickets += tickets_per_movie