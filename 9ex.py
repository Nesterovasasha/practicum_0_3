def calculate_passer_rating(ATT, COMP, YDS, TD, INT):
    a = ((COMP / ATT) - 0.3) * 5
    b = ((YDS / ATT) - 3) * 0.25
    c = (TD / ATT) * 20
    d = 2.375 - ((INT / ATT) * 25)

    a = max(0, min(a, 2.375))
    b = max(0, min(b, 2.375))
    c = max(0, min(c, 2.375))
    d = max(0, min(d, 2.375))

    passer_rating = ((a + b + c + d) / 6) * 100
    return passer_rating


ATT = int(input('Введите количество попыток паса (ATT): '))
COMP = int(input('Введите количество успешных пасов (COMP): '))
YDS = int(input('Введите количество ярдов за пас (YDS): '))
TD = int(input('Введите количество touchdown-пасов (TD): '))
INT = int(input('Введите количество перехваченных пасов (INT): '))

passer_rating = calculate_passer_rating(ATT, COMP, YDS, TD, INT)
print(f'Квотербек рейтинг игрока: {passer_rating:.2f}')