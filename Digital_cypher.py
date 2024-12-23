'''
Цифровой шифр присваивает каждой букве алфавита уникальный номер. Например:

 a  b  c  d  e  f  g  h  i  j  k  l  m
 1  2  3  4  5  6  7  8  9 10 11 12 13
 n  o  p  q  r  s  t  u  v  w  x  y  z
14 15 16 17 18 19 20 21 22 23 24 25 26

Вместо букв в зашифрованном слове мы пишем соответствующую цифру, например. Слово «разведчик»:

 s  c  o  u  t
19  3 15 21 20
Затем к каждой полученной цифре добавляем последовательные цифры из ключа. Например. В случае ключа, равного 1939 :

   s  c  o  u  t
  19  3 15 21 20
 + 1  9  3  9  1
 ---------------
  20 12 18 30 21

   m  a  s  t  e  r  p  i  e  c  e
  13  1 19 20  5 18 16  9  5  3  5
+  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  14 10 22 29  6 27 19 18  6  12 8
Задание
Напишите функцию, которая принимает строку str и число key и возвращает массив целых чисел, представляющих
закодированный str.

Ввод / вывод
Введённая строка str состоит только из строчных букв.
Введённое число key является положительным целым числом.

Пример
Encode("scout",1939);  ==>  [ 20, 12, 18, 30, 21]
Encode("masterpiece",1939);  ==>  [ 14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]
'''

import string


def encode(message, key):
    if len(message) == 0:
        return []
    num = index(message)
    encod = sum_num_key(num, key)
    return encod


def index(message):
    alf = string.ascii_lowercase
    num = []
    for i in message:
        num.append(alf.index(i) + 1)
    return num


def sum_num_key(num, key):
    l = (len(num) // len(f'{key}')) + 1
    k = (f'{key}') * l
    encod = []
    for i in range(len(num)):
        encod.append(num[i] + int(k[i]))
    return encod


if __name__ == '__main__':
    assert encode('', 12) == []
    assert index('a') == [1]
    assert index('ab') == [1, 2]
    assert sum_num_key([1, 2], 12) == [2, 4]
    assert encode('ab', 12) == [2, 4]
    print(encode("scout", 1939))
