'''
Уважаемый программист,
Мы в [SomeLargeCompany] решили расширить функциональность нашего онлайн-редактора текстов.
Мы написали новую функцию, которая принимает фразу, слово и массив индексов. Мы хотим, чтобы эта функция возвращала
фразу со словом, вставленным в каждый из индексов, указанных в массиве.
Однако наша текущая функция правильно выполняет только первую вставку, а все последующие — нет!
Пожалуйста, исправьте это для нас, и вы будете осыпаны деньгами.
Искренне ваш, [SomeLargeCompany]

Примечание :
индексы всегда находятся в диапазоне и передаются в виде отсортированного массива
примечание, если массив индексов пуст, просто верните начальную фразу

def insert_at_indexes(phrase, word, indexes):
    for i in indexes:
        phrase = phrase[:i] + word + phrase[i:]
    return phrase
'''

def insert_at_indexes(phrase, word, indexes):
    if len(indexes) == 0:
        return phrase
    else:
        count = 0
        for i in indexes:
            i += count
            phrase = phrase[:i] + word + phrase[i:]
            count += len(word)
        return phrase

if __name__ == '__main__':
    print(insert_at_indexes("I like codewars! It makes me happy.", " really", [1, 28]))
