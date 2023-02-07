# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

def first_non_repeating_letter(string):
    chars = list(string)

    for i in chars:
        if [x.lower() for x in chars].count(i.lower()) == 1:
            return i

    return ''
    