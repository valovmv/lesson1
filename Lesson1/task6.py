first_day = int(input('Введите растояние в первый день: '))
last_day = int(input('Введите растояние в последний день: '))
i = 1
while first_day < last_day:
    first_day *= 1.1
    i += 1
    print(i)
