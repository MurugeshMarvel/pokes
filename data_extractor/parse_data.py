import os 
from ccc import docx2txt as convert
def parse_dir(path):
	i =0
	for a,b,c in os.walk(path):
		#print '\n',c
		print '\n'
		c = str(c)
		file_path = a +  '/' +c
		print file_path
		#txt_val = convert.document_to_txt(file_path)
		i +=1
		print i

parse_dir('resumes/')