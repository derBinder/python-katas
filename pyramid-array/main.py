# https://www.codewars.com/kata/515f51d438015969f7000013/train/python

def pyramid(n):
    p = []

    for i in range(n):
        p.append([1] * (i + 1))

    return p
