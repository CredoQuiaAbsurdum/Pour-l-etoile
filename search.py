#!/usr/bin/python
# -*- coding:utf-8 -*-

from vocabulary import *
import sys


if __name__ == '__main__':
    try:
        target = sys.argv[1]
        word = LIST.search(str(target))
        print (str(word))

    except:
        print ("请输入词条")


