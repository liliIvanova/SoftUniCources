exam_hour = int(input())
exam_minute = int(input())

arrival_hour = int(input())
arrival_minute = int(input())

exam_minute += exam_hour * 60
arrival_minute += arrival_hour * 60

time_diff = exam_minute - arrival_minute
on_time_str = ''
minutes_str = ''
hours = 0
minutes = 0

if time_diff < 0:
    print('Late')
elif 0 <= time_diff <= 30:
    print('On time')
else:
    print('Early')

hours = abs(time_diff) // 60
minutes = abs(time_diff) % 60

if hours > 0:
    minutes_str = f'{hours}:{minutes:02d} hours '
else:
    minutes_str = f'{minutes} minutes '

if time_diff < 0:
    minutes_str += f'after the start'
else:
    minutes_str += f'before the start'

print(minutes_str)