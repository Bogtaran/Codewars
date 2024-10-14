"""Напишите функцию, persistence, которая принимает положительный параметр num и возвращает его мультипликативную
персистентность, то есть количество раз, в которое вы должны перемножать цифры num , пока не дойдете до однозначной
цифры.

Например, (Ввод -> Вывод):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
4 --> 0 (because 4 is already a one-digit number, there is no multiplication)"""


# В качестве предварительного упражнения: напишите функцию digits(x: int) -> List[int], которая возвращает список цифр
# десятичной записи числа х. Например, digits(47029) == [4,7,0,2,9].


'''Решение № 1'''
def persistence(n):
    count = 0
    if n // 10 == 0:
        return 0
    else:
        num = digits(n)
        count += 1

        while num // 10 != 0:
            num = digits(num)
            count += 1

        return count


def digits(n):
    n = f'{n}'
    num = 1
    list_digit = [int(i) for i in n]
    for i in list_digit:
        num *= i
    return num


'''Решение № 2'''
def persistence_2(n):
    count = 0
    if len(str(n)) == 1:
        return 0
    else:
        while len(str(n)) != 1:
            number = 1
            for i in str(n):
                number *= int(i)
            count += 1
            n = number
        return count


if __name__ == '__main__':
    print(persistence(39))
    print(persistence_2(39))
