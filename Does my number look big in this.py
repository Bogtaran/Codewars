"""Нарциссическое число (или Число Армстронга) - это положительное число, представляющее собой сумму собственных цифр,
каждая из которых возведена в степень числа цифр в заданном основании. В этом ката мы ограничимся десятичной дробью
(основание 10).

Например, возьмите 153 (3 цифры), что является нарциссическим:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
и 1652 (4 цифры), который не является:
    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
Задача:
Ваш код должен возвращать true или false (не 'true' и 'false') в зависимости от того, является ли данное число
нарциссическим числом в базе 10.
Это может быть True и False на вашем языке, например PHP.
Проверка ошибок на наличие текстовых строк или других недопустимых входных данных не требуется, в функцию будут
переданы только допустимые положительные ненулевые целые числа."""


def narcissistic(value):
    val = f'{value}'
    sum = 0
    for i in range(len(val)):
        sum += (int(val[i])) ** (len(val))
    return value == sum


if __name__ == '__main__':
    print(narcissistic(1652))

