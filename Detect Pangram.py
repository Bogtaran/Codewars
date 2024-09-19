"""
Панграмма - это предложение, которое содержит каждую букву алфавита по крайней мере по одному разу. Например,
предложение "Быстрая бурая лиса перепрыгивает через ленивую собаку" является панграммой, потому что в нем используются
буквы A-Z по крайней мере один раз (регистр значения не имеет).

По заданной строке определите, является ли она панграммой. Верните True, если это так, False, если нет. Игнорируйте
цифры и знаки препинания.
"""

def is_pangram(st):
    alf = 'abcdefghijklmnopqrstuvwxyz'
    st = st.lower()
    pangram = [i for i in alf if i in st]
    return len(pangram) >= 26



if __name__ == '__main__':
    print(is_pangram('l ;li^,X  X);f OHU\nD| 1+X\x0b_EA>BySglC2jutzg B4vi(QhwZ n,v\tg vQEmN7Uk-J+wFMrpA8x{'))