
import os
import converter_engine as convert

class converter:
    def __init__(self, source_name,dest_name, from_file, to_file ):
        output_string = convert_file(source_name, from_file, to_file)
        if '.' in dest_name:
            output_file_name = dest_name
        else:
            output_file_name = dest_name + '.' + to_file
        output_file = open(output_file_name,'w')
        output_file_name.write(output_string)
        output_file.close()

    def convert_file(self, file_name,from_file,to_file):
        if from_file == 'doc':
            if to_file == 'pdf':
                text_string = convert.doc2pdf(file_name)

            if to_file == 'txt':
                text_string = convert.doc2txt(file_name)

            else:
                print 'doc can be converted only to pdf,text using this program'

        elif from_file == 'pdf':
            if to_file == 'doc':
                text_string = convert.pdf2doc(file_name)
            elif to_file == 'txt':
                text_string = convert.pdf2txt(file_name)

        elif from_file == 'txt':
            if to_file == 'doc':
                text_string = convert.txt2doc(file_name)
            elif to_file == 'pdf':
                text_string = convert.txt2pdf(file_name)
        return text_string