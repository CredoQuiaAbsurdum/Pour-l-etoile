from vocabulary import *
import sys

if __name__ == '__main__':

    file = open('reverse.txt', 'w+')

if (len(sys.argv)>1):
    seed = sys.argv[1]
else:
    seed = 'Fox'
    LIST.shuffle(seed)

filename = 'version_%s.txt' % str(LIST.seed)
file = open(filename, 'w+')
file.write(str(LIST))
