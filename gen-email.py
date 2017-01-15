#!/bin/python2

from haikunator import Haikunator
from random import randrange
from names import get_first_name
from urllib import quote as urlquote

def random_line(filename):
    with open(filename) as afile:
        line = next(afile)
        for num, aline in enumerate(afile):
            if randrange(num + 2): continue
            line = aline
        return line.strip()

domains = ['gmail.com', 'gmail.com', 'gmail.com', 'gmail.com', 'gmail.com',
           'live.com', 'yahoo.com', 'ymail.com']

haikunator = Haikunator()
comps = haikunator.haikunate(delimiter='.', token_length=randrange(2) + 1).split('.')

if randrange(5) < 4:
    if randrange(4) < 3:
        user = random_line('indian-names/first')
    else:
        user = get_first_name().lower()
else:
    user = comps[0]

if randrange(2) == 1:
    user += '.'

if randrange(3) < 2:
    user += random_line('indian-names/last')
else:
    user += comps[1]

if randrange(4) < 3:
    if randrange(10) == 1:
        user += '.'
    user += comps[2]

print(urlquote(user + '@' + domains[randrange(len(domains))]))
