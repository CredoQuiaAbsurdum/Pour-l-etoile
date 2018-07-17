from vocabulary import *

if __name__ == '__main__':

    file = open('reverse.txt', 'w+')

    LIST.reverse()

    for each in LIST.words:
        try:
            temp = str(each)
        except:
            print(each.spelling.upper())

    file.write(str(LIST))
