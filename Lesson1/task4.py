number = int(input('Введите любое число: '))
ls = []
while number > 10:
    ls.append(number % 10)
    number //= 10
r = max(ls)
print(r)