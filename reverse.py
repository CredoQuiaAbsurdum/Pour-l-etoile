from vocabulary import *

if __name__ == '__main__':

    file = open('reverse.txt', 'w+')

    LIST.reverse()

filename = 'Reversed.txt'
file = open(filename, 'w+')
file.write(str(LIST))
