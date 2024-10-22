'''
Исправьте этот код так, чтобы он принимал один аргумент, x и возвращал "x больше нуля", если x положительно
(и не равно нулю), а в противном случае возвращал "x равно или меньше нуля". В обоих случаях замените x на фактическое
значение x.

Неверный код:
def corrections(x,y,z
    elif x > 0
        append float(x) + (is more than zero."
    elsse
        retorn float(x) + "is equal to or less than zero.)
'''

def corrections(x):
    if x > 0:
        return f"{x} is more than zero."
    else:
        return f"{x} is equal to or less than zero."


if __name__ == '__main__':
    print(corrections(5))
    print(corrections(0))
    print(corrections(-1))
