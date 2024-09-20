import math


def xp_to_target_lvl(current_xp, target_lvl):
    if type(current_xp) != int or type(target_lvl) != int or current_xp < 0 or 170 < target_lvl <= 0:
        return "Input is invalid."
    else:
        return level_analysis(target_lvl) - current_xp




def level_analysis(target_lvl):
    if target_lvl <= 10:
        return sum(des(target_lvl))
    else:
        list_ = des(10)
        c = list_[-1]

        for i in range(1, target_lvl//10+1):
            KOEFF = 0.25 - 0.01*i
            for j in range(target_lvl%10):
                c += math.floor(c * KOEFF)
                list_.append(c)
        return list_




def des(target_lvl):
    list_ = [314]
    c = 314
    for i in range(2, target_lvl):
        c += math.floor(c * 0.25)
        list_.append(c)
    return list_



if __name__ == '__main__':
    print(xp_to_target_lvl(0, 5))
