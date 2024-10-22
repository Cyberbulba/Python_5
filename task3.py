from random import randint


def move_rand(n):
    if n == 5 or n > 8:
        return n - randint(1, 3)
    if n <= 4:
        return 1
    if 6 <= n <= 8:
        return 5


def prov(x, n):
    return x.isdigit() and n - int(x) > 0 and 1 <= int(x) <= 3


def vvod(n):
    while True:
        x = input('Сколько камней вы хотите убрать: ')


n = randint(4, 30)
print(f'Всего {n} камней')
answer = input('Вы хотите делать ход первым? Если да, то нажмите +\n')
if answer == '+':
    while True:
        print(f'Ваш ход')
        n_del_player = vvod(n)
        n -= n_del_player
        print(f'Осталось {n} камней')
        if n == 1:
            exit('Победил игрок')
        print(f'Ходит робот')
        n = move_rand(n)
        print(f'Осталось {n} камней')
        if n == 1:
            exit('Победил робот')
else:
    while True:
        print(f'Ходит робот')
        n = move_rand(n)
        print(f'Осталось {n} камней')
        if n == 1:
            exit('Победил робот')
        print(f'Ваш ход')
        n_del_player = vvod(n)
        n -= n_del_player
        print(f'Осталось {n} камней')
        if n == 1:
            exit('Победил игрок')
