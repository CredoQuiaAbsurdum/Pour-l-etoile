#!/usr/bin/python
# -*- coding:utf-8 -*-

from vocabulary import *
import sys


if __name__ == '__main__':
    target = sys.argv[1]
    word = LIST.search(str(target))
    if word is not None:
        print (str(word))
    else:
        print ("词条%s未收录") % target

    # Get the synonyms
    if '-syn' in sys.argv:
        syns = []
        for tw in word.test_ways:
            if tw.synonyms is not None:
                syns += tw.synonyms
        print "近义词: %s" % ('   '.join(syns)).upper()
        count = 0
        for s in syns:
            syn = LIST.search(str(s))
            if syn is not None:
                print (str(syn))
                count += 1
        if count == 0:
            print ("未收录%s相关的近义词") % target
    
    # Get the synonyms
    if '-ant' in sys.argv:
        ants = []
        for tw in word.test_ways:
            if tw.antonyms is not None:
                ants += tw.antonyms
        print "反义词: %s" % ('   '.join(ants)).upper()
        count = 0
        for a in ants:
            ant = LIST.search(str(a))
            if ant is not None:
                print (str(ant))
                count += 1
        if count == 0:
            print ("未收录%s相关的反义词") % target

