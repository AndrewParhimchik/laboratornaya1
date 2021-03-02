import sys, math

a = int(sys.argv[1])
b = int(sys.argv[2])


def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    print("Наибольший общий делитель = " + str(b + a))


def nok(a, b):
    nod, nok = 0, 0
    c, d = a, b
    while c != 0 and d != 0:
        if c > d:
            c %= d
        else:
            d %= c
    nod = d + c
    nok = a * b // nod
    # использовал именно деление без остатка, так как остатка быть не может,
    # а вывод так работает красивее (без точки десятичной дроби)
    print("Наименьшее общее кратное = " + str(nok))

nok(a, b)

nod(a, b)
