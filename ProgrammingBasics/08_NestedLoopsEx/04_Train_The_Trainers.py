judges_num = int(input())
grades_total_sum = 0
grades_total_num = 0
ppt_num = 0

while True:
    ppt_name = input()

    if ppt_name == 'Finish':
        print(f'Student\'s final assessment is {grades_total_sum/grades_total_num:.2f}.')
        break
    else:
        ppt_num += 1
        grades_sum_per_ppt = 0

        for _ in range(judges_num):
            grade = float(input())
            grades_total_num += 1
            grades_sum_per_ppt += grade

        print(f'{ppt_name} - {grades_sum_per_ppt/judges_num:.2f}.')
        grades_total_sum += grades_sum_per_ppt
        grades_sum_per_ppt = 0
