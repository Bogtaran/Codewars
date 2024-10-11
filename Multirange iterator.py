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
    my_tuple = tuple(params)
    list_iter = []
    my_tuple = izm_params(my_tuple)
    list_iter.append(my_tuple)
    while my_tuple != (0,) * len(params):
        for j in range(len(params)):
            my_tuple = umen_params(my_tuple, j)
            list_iter.append(my_tuple)

    return print(list_iter)


def izm_params(params):
    my_tuple = tuple()
    for i in range(len(params)):
        if params[i] == 0:
            my_tuple += (0,)
        else:
            my_tuple += (params[i] - 1,)
    return my_tuple


def umen_params(params, j):
    my_tuple = tuple()
    if params[j] == 0:
        my_tuple += (0,)
    else:
        my_tuple += (params[j] - 1,)
    return my_tuple



if __name__ == '__main__':
    print((0,) * 3)
    multiiter(2, 3, 4)
