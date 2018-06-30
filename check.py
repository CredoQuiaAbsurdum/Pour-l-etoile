from vocabulary import *

if __name__ == '__main__':

    file = open('sample.txt', 'w+')

    LIST.shuffle()
    for each in LIST.words:
        try:
            temp = str(each)
        except:
            print(each.spelling.upper())

    file.write(str(LIST.get_list(1)))
