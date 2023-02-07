# https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
    x = url.split("/")

    if(x[0] == "https:" or x[0] == "http:"):
        x = x[2].split(".")
    else:
        x = x[0].split(".")

    if 'www' in x:
        x.remove('www')

    return x[0]
