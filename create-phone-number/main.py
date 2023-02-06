# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):
    s = ''.join([str(x) for x in n])
    return f'({s[:3]}) {s[3:6]}-{s[6:]}'