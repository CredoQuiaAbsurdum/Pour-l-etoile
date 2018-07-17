#!/usr/bin/python
# -*- coding:utf-8 -*-

from vocabulary import *
import sys


if __name__ == '__main__':
    filename = 'version_%s.txt' % str(LIST.version)
    file = open(filename, 'w+')
    file.write(str(LIST))


