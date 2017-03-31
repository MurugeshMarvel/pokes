import os


def parse_dir(path):
	for a,b,c in os.walk(path):
		print '\n',c
		print '\n'

parse_dir('resumes/')