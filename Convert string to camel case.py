"""Завершите метод / функцию так, чтобы она преобразовывала слова, разделенные тире / подчеркиванием, в верблюжий
 регистр. Первое слово в выходных данных должно быть написано с заглавной буквы, только если исходное слово было
  написано с заглавной буквы (известно как верхний регистр Camel, также часто называемый регистром Pascal).
   Следующие слова всегда должны быть написаны с заглавной буквы.

Примеры
"the-stealth-warrior" преобразуется в "theStealthWarrior"

"The_Stealth_Warrior" преобразуется в "TheStealthWarrior"

"The_Stealth-Warrior" преобразуется в "TheStealthWarrior"""


def to_camel_case(text):
    if len(text) >= 1:
        text2 = text[0] + text.title()[1:]
        new_text = [i for i in text2 if i.isalpha()]
        return ''.join(new_text)
    else:
        return ""


if __name__ == '__main__':
    print(to_camel_case("the-stealth-warrior"))


