"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    ...

    def __init__(self, path='words.txt'):
        self.path = path
        self.words = []
        self.get_word_count()

    def get_word_count(self):
        self.file = open(self.path, 'r')
        for word in self.file:
            self.words.append(word)
        self.file.close()
        print(f'{len(self.words)} words read')

    def random(self):
        rand_idx = random.randint(0, len(self.words)-1)
        return self.words[rand_idx][:-1]


class SpecialWordFinder(WordFinder):

    def __init__(self, path='diffWords.txt'):
        super().__init__(path)
        self.check_line()

    def check_line(self):
        rand_word = self.random()
        while rand_word == '' or rand_word.startswith('#') == True:
            rand_word = self.random()
        return rand_word
