# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    while len(str(n)) > 1:
        n = get_sum(n)
    return n

def get_sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum
