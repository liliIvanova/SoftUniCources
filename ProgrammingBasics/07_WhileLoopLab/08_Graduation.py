student_name = input()

grades_sum = 0
years_cnt = 0
failed_years_cnt = 0

while years_cnt < 12:
    grade = float(input())

    if grade < 4.00:
        failed_years_cnt += 1
        if failed_years_cnt > 1:
            failed_years_cnt = years_cnt + 1
            print(f'{student_name} has been excluded at {failed_years_cnt} grade')
            break
        continue
    grades_sum += grade
    years_cnt += 1

else:
    print(f'{student_name} graduated. Average grade: {grades_sum / 12:.2f}')

