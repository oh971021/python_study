# -*- coding: utf8 -*-

import sys

print(sys.version)

lol = [1,2,[3,4,5],[6,[7,8,9]]]

def flatten(lol):
    for item in lol :
        if isinstance(item, list) :
            for subitem in flatten(item) :
                yield subitem
        else :
            yield item

flatten(lol)

print(list(flatten(lol)))

def flatten_(lol) :
    for item in lol :
        if isinstance(item, list) :
            yield from flatten_(item)
        else :
            yield item

print(list(flatten_(lol)))