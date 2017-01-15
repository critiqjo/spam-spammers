#!/bin/python2

from random import randrange

prefixes = ['8075', '8173', '8169', '8369', '8999', '8700', '8660', '8668',
            '8919', '700', '701', '7020', '7021', '7977', '7978', '7989',
            '7990', '7991', '7', '8', '9']

num = prefixes[randrange(len(prefixes))]

while len(num) < 10:
    num += str(randrange(10))

print(num)
