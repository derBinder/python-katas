# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
    positions = []

    for i in list(text):
        if i.isalpha():
            positions.append(str(ord(i.lower()) - 96))

    return ' '.join(positions)
