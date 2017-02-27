#!/usr/bin/python

import os
import converter as converter_obj

class convert:
	def convert_file(self, filepath,save_path,from_file,to_file):
		if from_file == 'doc':
			if to_file == 'pdf':
				converter_obj.doc2pdf(filepath,save_path)

			if to_file == 'txt':
				converter_obj.doc2txt(filepath,save_path)

			if to_file == 'odt':
				converter_obj.doc2odt(filepath,save_path)

			else:
				print 'doc can be converted only to pdf,text and odt using this program'

		elif from_file == 'pdf':
			if to_file == 'doc':
				converter_obj.pdf2doc(filepath,save_path)
			elif to_file == 'txt':
				converter_obj.pdf2txt(filepath,save_path)
			elif to_file == 'odt':
				converter_obj.pdf2odt(filepath,save_path)

		elif from_file == 'txt':
			if to_file == 'doc':
				converter_obj.txt2doc(filepath,save_path)
			elif to_file == 'pdf':
				converter_obj.txt2pdf(filepath,save_path)

			elif to_file == 'odt':
				converter_obj.txt2odt(filepath,save_path)

		elif from_file == 'odt':
			if to_file == 'doc':
				converter_obj.odt2doc(filepath,save_path)
			elif to_file == 'pdf':
				converter_obj.odt2doc(filepath,save_path)
			elif to_file == 'txt':
				converter_obj.odt2txt(filepath,save_path)



	def convert_file_in_folder(self,filepath,save_path,from_file,to_file,all='no'):
		if all == 'yes':
			for file_name in os.listdir(filepath):
				if from_file == 'doc':
					if to_file == 'pdf':
						converter_obj.doc2pdf(filepath,save_path)

					if to_file == 'txt':
						converter_obj.doc2txt(filepath,save_path)

					if to_file == 'odt':
						converter_obj.doc2odt(filepath,save_path)

					else:
						print 'doc can be converted only to pdf,text and odt using this program'

				elif from_file == 'pdf':
					if to_file == 'doc':
						converter_obj.pdf2doc(filepath,save_path)
					elif to_file == 'txt':
						converter_obj.pdf2txt(filepath,save_path)
					elif to_file == 'odt':
						converter_obj.pdf2odt(filepath,save_path)

				elif from_file == 'txt':
					if to_file == 'doc':
						converter_obj.txt2doc(filepath,save_path)
					elif to_file == 'pdf':
						converter_obj.txt2pdf(filepath,save_path)

					elif to_file == 'odt':
						converter_obj.txt2odt(filepath,save_path)

				elif from_file == 'odt':
					if to_file == 'doc':
						converter_obj.odt2doc(filepath,save_path)
					elif to_file == 'pdf':
						converter_obj.odt2doc(filepath,save_path)
					elif to_file == 'txt':
						converter_obj.odt2txt(filepath,save_path)






