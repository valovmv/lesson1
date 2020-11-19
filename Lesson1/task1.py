print('Добрый вечер')
name = input('Введите ваше имя: ')
age = int(input('Введите Ваш возраст: '))
age10 = int(age + 10)
#print(age10)
while True:
    if age10 >= 30:
        print('Добро пожаловать')
        break
    else:
        print('Вход воспрещен')
        break
print('end')
