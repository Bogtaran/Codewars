'''
https://www.codewars.com/kata/55466989aeecab5aac00003e/train/python
'''


def sq_in_rect(lng, wdth):
    sq_list = []
    if lng == wdth:
        return None
    else:
        while lng - wdth != 0:
            if lng < wdth:
                lng, wdth = wdth, lng
            num = wdth
            sq_list.append(num)
            lng = lng - wdth
        num = lng
        sq_list.append(num)

    return sq_list


if __name__ == '__main__':
    print(sq_in_rect(20, 14))
