#!/usr/bin/python


letter = []
words = []
file = open("sample.doc",'r')
document =  file.read()
leng = len(document)
count = 0
for word in document:
	if count < leng:
		if word != ' ':
			words.append(word)

		else:
			act_words = ''.join(words)
			letter.append(act_words)
			del words[:]

	
	
	else:
		last_word = ''.join(words)
		letter.append(act_words)
		break

	print words
	count+=1
print letter[9]
