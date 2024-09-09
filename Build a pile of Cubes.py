"""https://www.codewars.com/kata/5592e3bd57b64d00f3000047"""

def find_nb(m):
    if m == 1:
        return 1
    else:
        for n in range(2, m):
            a = n ** 3
            if a > m:
                return -1
            elif a == m:
                return n
            else:
                for x in range(1,n):
                    a += (n - x) ** 3
                if a == m:
                    return n









