# https://www.codewars.com/kata/52549d3e19453df56f0000fe/train/python

def fib(n):
    a = 0
    b = 1

    for i in range(n - 1):
        c = a + b
        a = b
        b = c

    return a
