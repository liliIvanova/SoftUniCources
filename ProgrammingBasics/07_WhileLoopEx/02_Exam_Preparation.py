low_grades_number = int(input())

average_grade = 0
sum_of_grades = 0
num_of_received_low_grades = 0
number_of_problems = 0
last_problem_name = ''

while True:
    if num_of_received_low_grades == low_grades_number:
        print(f"You need a break, {low_grades_number} poor grades.")
        break

    problem_name = input()

    if problem_name == 'Enough':
        print(f'Average score: {average_grade:.2f}\n'
              f'Number of problems: {number_of_problems}\n'
              f'Last problem: {last_problem_name}')
        break
        

    grade_new = int(input())

    if grade_new <= 4:
        num_of_received_low_grades += 1

    number_of_problems += 1
    sum_of_grades += grade_new
    average_grade = sum_of_grades/ number_of_problems
    last_problem_name = problem_name


