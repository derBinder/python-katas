# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    word = word.lower()
    new_word = []

    for i in word:
        if word.count(i) == 1:
            new_word.append('(')
        else:
            new_word.append(')')
    
    return ''.join(new_word)
    