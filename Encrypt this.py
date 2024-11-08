'''
Описание:
Зашифруйте это!

Вы хотите создавать секретные сообщения, которые можно расшифровать с помощью «Расшифруй это!» kata. Вот условия:

Ваше сообщение представляет собой строку, содержащую слова, разделенные пробелами.
Вам необходимо зашифровать каждое слово в сообщении, используя следующие правила:
Первая буква должна быть преобразована в ее ASCII-код.
Вторую букву необходимо заменить последней буквой
Всё просто: во вводе нет специальных символов.

Примеры:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
'''


def encrypt_this(text):
    text = text.split()
    new_t = []
    for i in text:
        if len(i) == 1:
            new_t.append(str(ord(i[0])))
        elif len(i) == 2:
            new_t.append(str(ord(i[0])) + i[1])
        else:
            new_t.append(str(ord(i[0])) + i[-1] + i[2:-1] + i[1])

    return ' '.join(new_t)


if __name__ == '__main__':
    print(encrypt_this('Hello'))
