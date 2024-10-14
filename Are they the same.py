"""
Учитывая два массива, a и b напишите функцию comp(a, b) , которая проверяет, имеют ли два массива "одинаковые"
элементы с одинаковыми кратностями (кратность элемента - это количество раз, когда он появляется). "То же самое"
здесь означает, что элементы в b являются элементами в a возведены в квадрат, независимо от порядка.

Примеры
Допустимые массивы
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) возвращает true, потому что в b 121 - это квадрат из 11, 14641 - это квадрат из 121, 20736 - квадрат из 144,
361 - квадрат из 19, 25921 - квадрат из 161 и так далее. Это становится очевидным, если мы напишем b элементы в виде
квадратов:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Недопустимые массивы
Если, например, мы изменим первое число на что-то другое, comp больше не возвращает true:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) возвращает false, потому что в b 132 не является квадратом какого-либо числа a.

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) возвращает false, потому что в b 36100 не является квадратом какого-либо числа a.

Примечания
a или b может быть [] or {}

a или b может быть None
Если a или b являются nil (или null or None, в зависимости от языка), проблема не имеет смысла, поэтому верните false .
"""


def comp(array1, array2):
    if type(array1) not in (list, set) or type(array2) not in (list, set):
        return False
    else:
        array1 = [i**2 for i in array1]
        array2 = [j for j in array2]
        return sorted(array1) == sorted(array2)


if __name__ == '__main__':
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    print(comp(a,b))


