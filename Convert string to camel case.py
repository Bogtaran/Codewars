"""Завершите метод / функцию так, чтобы она преобразовывала слова, разделенные тире / подчеркиванием, в верблюжий
 регистр. Первое слово в выходных данных должно быть написано с заглавной буквы, только если исходное слово было
  написано с заглавной буквы (известно как верхний регистр Camel, также часто называемый регистром Pascal).
   Следующие слова всегда должны быть написаны с заглавной буквы.

Примеры
"the-stealth-warrior" преобразуется в "theStealthWarrior"

"The_Stealth_Warrior" преобразуется в "TheStealthWarrior"

"The_Stealth-Warrior" преобразуется в "TheStealthWarrior"""

def to_camel_case(text):
    text2 = text.title()
    new_text = ''
    for i in text2:
        if i.isalpha():
            new_text += i
    new_text = text[0] + new_text[1:]
    return new_text



