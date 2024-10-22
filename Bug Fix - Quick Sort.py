'''
Существует реализация алгоритма быстрой сортировки. Ваша задача — исправить её. Все входные данные верны.

def quicksort(arr):
	if len(arr) < 1: return arr
	p = arr[0]
	return quicksort(map(lambda x: x < p, arr[::-1])) + quicksort(map(lambda x: x > p, arr[2:]))
'''


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        p = arr[0]
        L = [x for x in arr if x < p]
        S = [x for x in arr if x == p]
        R = [x for x in arr if x > p]
    return quicksort(L) + S + quicksort(R)


if __name__ == '__main__':
    print(quicksort([3, 1, -5, 10, 2, 5, 4, 1, 7]))
