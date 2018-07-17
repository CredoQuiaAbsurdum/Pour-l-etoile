#!/usr/bin/python
# -*- coding:utf-8 -*-

from tools import *
import random

EMPTYLIST = 'Empty List'
class VocabularyList(object):

    def __init__(self, words = []):
        self.words = words
        self.seed = None
        self.version = 'Alphabetical Order'

    def __str__(self):
        try:
            if (len(self.words)==3100):
                if self.seed:
                    filecontent = 'VERSION: %s' % self.seed
                else:
                    filecontent = 'VERSION: %s' % self.version
                for i in range(3100):
                    if (i%100==0):
                        filecontent += '\n\n\n------------- LIST %s -------------' % (i/100+1)
                    if (i%10==0):
                        filecontent += '\n\n\n*** Unit %s.%s ***\n\n' % ((i/100+1), (i%100/10+1))
                        filecontent += enumerate_list(self.words[i:i+10])
                return filecontent
            else:
                return enumerate_list(self.words)
        except:
            return EMPTYLIST+': output failed'

    def add_word(self, w):
        if self.words is None:
            self.words = []
        add_to_list(w, self.words)


    def add_list(self, v):
        if v.words is not None:
            self.words += v.words

    def only_words(self):
        text = []
        for word in self.words:
            text.append(word.spelling)
        return '   '.join(text)

    def words_or_def(self):
        # a word would have multiple testways
        pass

    def search(self, w):
        for word in self.words:
            if (word.spelling.lower() == w.lower()):
                return str(word)
        return "词条 %s 未收录" % w

    def shuffle(self, seed='Fox'):
        self.seed = seed
        try:
            random.Random(seed).shuffle(self.words)
        except:
            return EMPTYLIST+': shuffle failed.'

    def reverse(self):
        self.words.sort(key=lambda x: x.spelling[::-1])
        self.version = 'Reverse'

    def get_list_unit(self, listNum, unitNum):
        if (len(self.words)==3100):
            start = (listNum-1)*100+(unitNum-1)*10
            end = start+10
            return VocabularyList(self.words[start:end])
        else:
            return 'This is not a whole list.'

    def get_list(self, listNum):
        if (len(self.words)==3100):
            content = '\n\n\n------------- LIST %s -------------' % listNum
            for unitNum in range(1, 11):
                content += '\n\n\n*** Unit %s ***\n\n' % unitNum
                start = (listNum-1)*100+(unitNum-1)*10
                end = start+10
                content += enumerate_list(self.words[start:end])
            return content
        else:
            return 'This is not a whole list.'

class Word(object):

    def __init__(self, spelling, pronunciation, test_ways):
        self.spelling = spelling.lower().capitalize()
        self.pronunciation = pronunciation
        self.test_ways = test_ways

    def __str__(self):
        spelling = self.spelling
        if self.pronunciation != '':
            pronunciation = '[' + self.pronunciation + ']'
        else:
            pronunciation = ''
        test_ways = ''
        for _ in self.test_ways:
            test_ways += "\n【考法 %s】 %s" % (self.test_ways.index(_)+1, str(_))
        return '%s %s %s\n' % (spelling, pronunciation, test_ways)

    def show_translation(self):
        translation = []
        for each in self.test_ways:
            translation.append(each.get_translation())
        return '; '.join(translation)

class TestWay(object):

    def __init__(self, part_of_speech, translation, definition, examples = None, synonyms = None, antonyms = None, other_form = None):
        self.part_of_speech = part_of_speech
        self.translation = translation
        self.definition = definition
        self.examples = examples
        self.synonyms = synonyms
        self.antonyms = antonyms
        self.other_form = other_form

    def __str__(self):
        # may need a different way for new line in rtf
        part_of_speech = self.part_of_speech + '.'
        examples = ''
        other_form = ''
        synonyms = ''
        antonyms = ''
        if self.examples is not None:
            examples = '\n【例】' + '\n【例】'.join(self.examples)
        if self.other_form is not None:
            other_form = '\n【派】' + self.other_form
        if self.synonyms is not None:
            synonyms = '\n【近】' + ', '.join(self.synonyms)
        if self.antonyms is not None:
            antonyms = '\n【反】' + ', '.join(self.antonyms)
        return '%s %s: %s %s %s %s %s' % (part_of_speech, self.translation, self.definition, examples, other_form, synonyms, antonyms)

    def get_translation(self):
        return self.part_of_speech+'. '+self.translation

