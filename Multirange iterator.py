"""
Давайте посмотрим на следующий генератор:

def gen():
    for i in range(2):
        for j in range(3):
            yield (i, j)

Если мы выведем все полученные значения, то получим

(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
Для заданного списка параметров N вы должны вернуть итератор, который проходит через все возможные кортежи A, где Ai
изменяется с 0 на Ni.
"""

def multiiter(*params):
    params = list(params)
    if len(params) == 1:
        for i in range(params[0]):
            yield (i,)
    else:
        for i in range(params[0]):
            for j in range(params[1]):
                yield (i, j)


gen = multiiter(2)


if __name__ == '__main__':
    for i in gen:
        print(i)
