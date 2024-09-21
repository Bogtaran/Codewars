"""
Напишите функцию, которая при задании URL в виде строки анализирует только доменное имя и возвращает его в виде
строки.
Например:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""
def domain_name(url):
    domain = ''
    if url.count('http://') == 1:
        url = url.replace('http://', '')
        if url.count('www.') == 1:
            url = url.replace('www.', '')
            ind = url.find('.')
        else:
            ind = url.find('.')
    elif url.count('https://') == 1:
        url = url.replace('https://', '')
        ind = url.find('.')
    elif url.count('www.') == 1:
        url = url.replace('www.', '')
        ind = url.find('.')
    elif url.count('.') >= 1:
        ind = url.find('.')
    domain = url[:ind]
    return domain


def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]


def domain_name(url):
    url = url.replace('www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')

    return url[0:url.find('.')]
