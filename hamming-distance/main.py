# https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69/train/python

def hamming(a,b):
    return sum(1 for i, j in zip(a, b) if i != j)
    