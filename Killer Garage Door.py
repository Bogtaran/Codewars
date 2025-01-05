"""
Ситуация
Вас наняла компания, производящая электрические гаражные ворота. Несчастные случаи с нынешней линейкой продукции привели к многочисленным повреждениям автомобилей, переломам и гибели нескольких домашних животных. Ваша задача — написать более безопасную версию программного обеспечения для их контроллера.

Спецификация
Мы всегда начинаем с закрытой двери. На пульте дистанционного управления есть ровно одна кнопка, которая работает следующим образом.

Если дверь закрыта, нажатие на кнопку открывает её, и наоборот
Для полного открытия или закрытия двери требуется 5 секунд
Пока дверь движется, один толчок останавливает движение, другой толчок возобновляет движение в том же направлении
Чтобы сделать дверь более безопасной, она оснащена системой обнаружения препятствий на основе сопротивления.
При обнаружении препятствия дверь должна немедленно изменить направление движения.

Входные данные
Строка, в которой каждый символ представляет одну секунду, со следующими возможными значениями.

'.' Никакого события
'P' Кнопка была нажата
'O' Обнаружено препятствие (заменяет P)
Например, '..P....' означает, что в течение двух секунд ничего не происходит, затем нажимается кнопка, после чего никаких дальнейших событий не происходит.

Выходной сигнал
Строка, в которой каждый символ обозначает одну секунду и указывает положение двери (0 — полностью закрыта, 5 — полностью открыта). Дверь начинает двигаться немедленно, поэтому её положение меняется в ту же секунду, что и событие.

Пример
..P...O..... как входные данные должны давать результат 001234321000 как выходные
"""


def controller2(events):
    output = ''
    close = True
    number = 0
    counter = 0
    stop = False
    closed_process = False
    opening_process = False
    for i in events:
        if number == 0:
            if i == '.':
                counter += 1
                output += f'{number}'
            elif i == 'P':
                counter += 1
                number = 1
                opening_process = True
                output += f'{number}'
        elif 0 < number < 5:
            if i == '.' and stop:
                counter += 1
                output += f'{number}'
            elif i == 'P' and stop and opening_process:
                counter += 1
                number -= 1
                stop = False
                opening_process = False
                closed_process = True
                output += f'{number}'
            elif i == 'P' and stop and closed_process:
                counter += 1
                number -= 1
                stop = False
                opening_process = True
                closed_process = False
                output += f'{number}'
            elif i == '.' and opening_process:
                counter += 1
                number += 1
                output += f'{number}'
            elif i == '.' and closed_process:
                counter += 1
                number -= 1
                output += f'{number}'
            elif i == 'P' and opening_process:
                counter += 1
                stop = True
                output += f'{number}'
            elif i == 'P' and closed_process:
                counter += 1
                stop = True
                output += f'{number}'
            elif i == 'O' and opening_process:
                counter += 1
                opening_process = False
                closed_process = True
                number -=1
                output += f'{number}'
            elif i == 'O' and closed_process:
                counter += 1
                opening_process = True
                closed_process = False
                number += 1
                output += f'{number}'
        elif number == 5:
            opening_process = False
            if i == '.':
                counter += 1
                output += f'{number}'
            elif i == 'P':
                counter += 1
                number = 4
                closed_process = True
                output += f'{number}'

    return output


if __name__ == '__main__':
    print(controller2('....'))
    print(controller2('.P.........'))
    print(controller2('.P......P..'))
    print(controller2('.P...P..'))
    print(controller2('.P...P..P....'))
