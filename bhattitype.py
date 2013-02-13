'''Library for making regular speak into Bhatti Type!

Resources:
http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings
http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines
http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/Grammar_and_Misc

http://grammar.yourdictionary.com/spelling-and-word-lists/misspelled.html
http://grammar.yourdictionary.com/spelling-and-word-lists/150more.html

http://nltk.org/book/ch01.html
'''

import csv
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
				self.misspellings[correct_spelling] = misspelling
		fp.close()
	
	def _convert_token(self, input):
		if input in self.misspellings:
			return self.misspellings[input]
		return input
	
	def convert(self, input):
		return " ".join(map(self._convert_token, input.split()))


if __name__ == "__main__":
	input = " ".join(sys.argv[1:])
	print "input: %s" % input
	bt = BhattiType()
	output = bt.convert(input)
	print "output: %s" % output
