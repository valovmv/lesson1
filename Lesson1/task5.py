profit = int(input('Введите значение выручки вашей фирмы: '))
cost = int(input('Введите значение издержек фирмы: '))
result = profit - cost
# print(result)
while True:
    if result > 0:
        workers = int(input('Какое количество сотруников у вас работает? '))
        profit_one = result / workers
        print(profit_one)
        print('Поздравляю, ваша фирма в плюсе')
        break
    elif result < 0:
        print('Очень жаль, фирма несет убытки')
        break
print('End')
