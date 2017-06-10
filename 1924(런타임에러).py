x, y = [int(i) for i in input().split()]

days = -1
_data = [31,28,31,30,31,30,31,31,30,31,30,31]
_day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

for i in range(0, x-1):
    days += _data[i]
days += y

print(_day[days])