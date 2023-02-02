# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python

def rot13(message):
    rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                               'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    return message.translate(rot13trans)
