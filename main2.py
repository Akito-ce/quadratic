while True:
    a = input()
    if a.isdigit() and a != '0':
        a = float(a)
        break
    else:
        print('Введите другое значение')

b, c = float(input()), float(input())

d = b ** 2 - 4 * a * c
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)
if d > 0:
    print(f'x1 = {x1}\nx2 = {x2}')
elif d == 0:
    print(f'x = {x1}')
else:
    print('Корней нет')
