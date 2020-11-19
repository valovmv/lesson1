import datetime
time_second = int(input('Введите время в секундах: '))
time_hours = str(datetime.timedelta(seconds = time_second))
print(time_hours)

print('end')