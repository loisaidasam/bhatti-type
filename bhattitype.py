'''Library for converting regular text into Bhatti Type!

Resources:
http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings
http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines

Other ideas:
http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/Grammar_and_Misc
http://grammar.yourdictionary.com/spelling-and-word-lists/misspelled.html
http://grammar.yourdictionary.com/spelling-and-word-lists/150more.html
http://nltk.org/book/ch01.html
'''

import csv
import random
import string
import sys


class BhattiType(object):
    def __init__(self):
        self._setup_misspellings()

    def _setup_misspellings(self):
        self.misspellings = {}
        fp = open('misspellings.csv')
        reader = csv.reader(fp)
        for line in reader:
            misspelling = line[0]
            correct_spellings = line[1:]
            for correct_spelling in correct_spellings:
                if correct_spelling not in self.misspellings:
                    self.misspellings[correct_spelling] = []
                self.misspellings[correct_spelling].append(misspelling)
        fp.close()

    def _convert_token(self, input):
        before = ''
        for c in input:
            if c not in string.punctuation:
                break
            before += c
        after = ''
        # string reversal (via http://stackoverflow.com/questions/931092/reverse-a-string-in-python)
        for c in input[::-1]:
            if c not in string.punctuation:
                break
            after = c + after
        meat = input[len(before):]
        meat = meat[:(len(meat) - len(after))]
        if meat not in self.misspellings:
            return input
        key = random.randint(0, len(self.misspellings[meat])-1)
        return (before + self.misspellings[meat][key] + after)

    def convert(self, input):
        return " ".join(map(self._convert_token, input.split()))


if __name__ == "__main__":
    q = " ".join(sys.argv[1:] or '')
    print "q:", q
    bt = BhattiType()
    result = bt.convert(q)
    print "result:", result
