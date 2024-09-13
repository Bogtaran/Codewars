"""
Реализуйте функцию unique_in_order, которая принимает в качестве аргумента последовательность и возвращает список
элементов без каких-либо элементов с одинаковым значением рядом друг с другом и сохраняет исходный порядок элементов.

Например:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""

def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    new_sequence = [sequence[0]]
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i - 1]:
            new_sequence.append(sequence[i])
            i = i + 1
        else:
            i = i + 1

    return new_sequence


if __name__ == '__main__':
    print(unique_in_order('AAAABBBCCDAABBB'))
