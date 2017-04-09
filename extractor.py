import csv
import itertools
import nltk
import numpy as np
import theano.tensor as Ten



with path as open('data/')
print path[:10]

vocabulary_size = 80000
unknown_token = "UNKNOWN_TOKEN"
sentence_start_token = "SENTENCE_START"
sentence_end_token = "SENTENCE_END"


print "REading the CSV"
with open('reddit.csv','rb') as f:
	reader = csv.reader(f, skipinitialspace=True)
	string = reader.next()
	sentences = itertools.chain(*[nltk.sent_tokenize(x[0].decode('utf-8').lower()) for x in reader])
	sentences = ['%s %s %s' % (sentence_start_token, x , sentence_end_token) for x in sentences]

print "Parsed %d Sentences" %(len(sentences))

tokenized_sentences = [nltk.word_tokenize(sent) for sent in sentences]

word_freq = nltk.FreqDist(itertools.chain(*tokenized_sentences))
print "Found %d unique words tokens." % len(word_freq.items())

vocab = word_freq.most_common(vocabulary_size-1)
index_to_word = [x[0] for x in vocab]
index_to_word.append(unknown_token)
'''for i,w in enumerate(index_to_word):
	print i,'**',w'''
word_to_index = dict([(w,i) for i,w in enumerate(index_to_word)])

print "Using the Vocabulary size of %d " %(vocabulary_size)
print "The least Frequent word in our Vocabulary is '%s' and appeared %d times " % (vocab[-1][0],vocab[-1][1])

for i, sent in enumerate(tokenized_sentences):
	tokenized_sentences[i] = [w if w in word_to_index else unknown_token for w in sent]

print "\n Example Sentence : %s" % sentences[0]
print "\n Example Sentence after Pre_processing -- '%s'" % tokenized_sentences[0]
