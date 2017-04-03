import os
import subprocess
import array
import nltk
import itertools

def get_name(doc):
	text = open(doc)
	char = text.read()
	char = char.lower()
	word = nltk.word_tokenize(char.decode('utf-8'))
	word_freq = nltk.FreqDist(itertools.chain(*word))
	print "Found %d unique words" %len(word_freq)
	vocab = 
get_name('data/data/anvitha.txt')