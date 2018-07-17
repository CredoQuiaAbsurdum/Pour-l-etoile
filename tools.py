#!/usr/bin/python
# -*- coding:utf-8 -*-

def enumerate_list(list):
    return ("\n".join(map(str,list)))

# Add some item(s) to a list
def add_to_list(someI, someList):
    try:
        someList += someI
    except:
        someList.append(someI)

def random(num):
    import random
    a = []
    for _ in range(1, num+1):
        a.append(_)
    return a[0]

def son():
    print '爸爸'

# Read syn and ant for TestWay
def getlist(L):
    if type(L) is list:
        return L
    elif type(L) is str:
        return L.split(', ')
    else:
        return []



# Text attributes
ALL_ATTRIBUTES_OFF = 0
BOLD = 1
UNDERSCORE = 4
BLINK = 5
REVERSE = 7
CONCEAL = 8
# Foreground colors
BLACK_FG = 30
RED_FG = 31
GREEN_FG = 32
YELLOW_FG = 33
BLUE_FG = 34
MAGENTA_FG = 35
CYAN_FG = 36
WHITE_FG = 37
# Background colors
BLACK_BG = 40
RED_BG = 41
GREEN_BG = 42
YELLOW_BG = 43
BLUE_BG = 44
MAGENTA_BG = 45
CYAN_BG = 46
WHITE_BG = 47

# improve by using *args
def set_graphics_mode(attr1, attr2 = None, attr3 = None):
    if attr2 is not None:
        if attr3 is not None:
            return '\033[%s;%s;%sm' % (str(attr1), str(attr2), str(attr3))
        return '\033[%s;%sm' % (str(attr1), str(attr2))
    return '\033[%sm' % str(attr1)
