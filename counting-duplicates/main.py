# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    duplicates = {}

    for i in list(text):
        i = i.lower()
        if i not in duplicates.keys():
            duplicates[i] = 1
        else:
            duplicates[i] += 1

    return len({k: v for k, v in duplicates.items() if v > 1})
     