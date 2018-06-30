#!/usr/bin/python
# -*- coding:utf-8 -*-

from vocabulary import *
import sys


if __name__ == '__main__':
    # Generate shuffled vocabulary
    if (len(sys.argv)>1):
        # Generate shuffled vocabulary
        if(sys.argv[1]=='-shuffle'):
            if (len(sys.argv)==2):
                LIST.shuffle()
            else:
                seed = ' '.join(map(str, sys.argv[2:]))
                LIST.shuffle(seed)
            filename = 'version_%s.txt' % str(LIST.seed)
            file = open(filename, 'w+')
            file.write(str(LIST))

        # Search a word
        if(sys.argv[1]=='-search'):
            try:
                if (len(sys.argv)>2):
                    word = LIST.search(str(sys.argv[2]))
                    print (word)
                else:
                    print ("请输入词条")
            except:
                print ("词条 %s 不合法" % sys.argv[2])

    #LIST.shuffle('Francis')



