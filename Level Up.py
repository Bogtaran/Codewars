"""
В этом Ката вы являетесь разработчиком игры и запрограммировали MMORPG № 1 (многопользовательскую онлайн-ролевую игру)
по всему миру!!! Вам пришло много предложений по улучшению игры, одно из которых вас заинтересовало, и вы сразу же
начнете над ним работать. Игроки в игре имеют уровни от 1 до 170, XP (сокращение от experience) требуется для
повышения уровня игрока и получается за выполнение всевозможных действий в игре, новый игрок начинает с 1 уровня с 0 XP.
Вы хотите добавить функцию, которая позволила бы игроку вводить целевой уровень, а на выходе было бы указано, сколько
опыта игрок должен получить, чтобы достичь целевого уровня ... просто, да. Создайте функцию с именем xp_to_target_lvl,
которая принимает 2 аргумента (current_xp и target_lvl, оба как целое число) и возвращает оставшийся опыт для
достижения игроком target_lvl в формате округленного в меньшую сторону целого числа. Для повышения уровня с 1 по 2
требуется 314 опыта, сначала для каждого повышения уровня требуется на 25% опыта больше, чем для предыдущего
повышения уровня, каждые 10 уровней процентное увеличение уменьшается на 1. Смотрите примеры для лучшего понимания.
Имейте в виду, что когда игроки достигают 170 уровня, они прекращают повышать уровень, но продолжают набираться опыта.
Если один или оба аргумента недопустимы (не указаны, не в правильном формате, не в диапазоне ... и т.д.), верните
"Ввод недопустим"...Если игрок уже достиг target_lvl возврата"You have already reached level target_lvl.".

Примеры:

xp_to_target_lvl(0,5) => XP from lvl1 to lvl2 = 314
                         XP from lvl2 to lvl3 = 314 + (314*0.25) = 392
                         XP from lvl3 to lvl4 = 392 + (392*0.25) = 490
                         XP from lvl4 to lvl5 = 490 + (490*0.25) = 612
                         XP from lvl1 to target_lvl = 314 + 392 + 490 + 612 = 1808
                         XP from current_xp to target_lvl = 1808 - 0 = 1808

xp_to_target_lvl(12345,17) => XP from lvl1 to lvl2 = 314                   
                               XP from lvl2 to lvl3 = 314 + (314*0.25) = 392
                               XP from lvl3 to lvl4 = 392 + (392*0.25) = 490
                               ...
                               XP from lvl9 to lvl10 = 1493 + (1493*0.25) = 1866 
                               XP from lvl10 to lvl11 = 1866 + (1866*0.24) = 2313 << percentage increase is 
                               ...                                                   reduced by 1 (25 - 1 = 24)
                               XP from lvl16 to lvl17 = 6779 + (6779*0.24) = 8405
                               XP from lvl1 to target_lvl = 314 + 392 + 490 + 612 + ... + 8405 = 41880
                               XP from current_xp to target_lvl = 41880 - 12345 = 29535

xp_to_target_lvl() => "Input is invalid."             }
xp_to_target_lvl(-31428.7,'47') => "Input is invalid." }> Invalid input
xp_to_target_lvl(83749,0) => "Input is invalid."   }

xp_to_target_lvl(2017,4) => "You have already reached level 4."
xp_to_target_lvl(0,1) => 'You have already reached level 1.'

Обязательно округляйте количество опыта, необходимое для каждого повышения уровня, округление в большую сторону
приведет к тому, что результат будет немного неправильным.
"""

import math

def xp_to_target_lvl(current_xp=-1, target_lvl=-1):
    if type(current_xp) != int or type(target_lvl) != int or current_xp < 0 or 170 < target_lvl or target_lvl <= 0:
        return "Input is invalid."
    elif current_xp == -1 and target_lvl == -1:
        return "Input is invalid."
    elif current_xp==0 and target_lvl == 1:
        return f"You have already reached level {target_lvl}."
    else:
        if level_analysis(target_lvl) <= current_xp:
            return f"You have already reached level {target_lvl}."
        else:
            return level_analysis(target_lvl) - current_xp


def level_analysis(target_lvl):
    _sum_ = 314
    c = 314
    for i in range(2, target_lvl):
        KOEFF = 0.25 - 0.01 * (i // 10)
        c += math.floor(c * KOEFF)
        _sum_ += c
    return _sum_


if __name__ == '__main__':
    print(xp_to_target_lvl(0, 15))