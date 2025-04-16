from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления'
           'квадратного корня из заданного числа')

print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень"""
    krn = sqrt(number)
    return print(f'Мы вычислили квадратный корень из введённого вами числа.'
                 f'Это будет: {krn}')


def calc(your_number):
    """Проверка числа"""
    if your_number <= 0:
        root = 0
    else:
        root = calculate_square_root(your_number)
    return root


calc(36)
