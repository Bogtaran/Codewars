def multiiter(*params):
    my_tuple = tuple(params)
    if len(my_tuple) == 1:
        if my_tuple == (0,):
            return []
        else:
            for i in initial_list(params):
                yield i


    else:
        list_iter = initial_list(my_tuple)
        for j in my_tuple[1:]:
            list_iter = increase_list(list_iter, j)

        for i in list_iter:
            yield i


def initial_list(my_tuple):
    list_iter = []
    for i in range(my_tuple[0]):
        list_iter.append((i,))
    return list_iter


def increase_list(list_iter, j):
    new_list_iter = []
    for a in list_iter:
        for i in range(j):
            new_list_iter.append(a + (i,))
    return sorted(new_list_iter)


if __name__ == '__main__':
    multiiter(2, 3, 4)
