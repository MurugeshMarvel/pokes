from subprocess import Popen, PIPE
from docx import opendocx, getdocumenttext
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path,'r')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

def document_to_text(filename):
    if filename[-4:] == ".doc":
        cmd = ['antiword', filename]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('ascii', 'ignore')
    elif filename[-5:] == ".docx":
        document = opendocx(filename)
        paratextlist = getdocumenttext(document)
        newparatextlist = []
        for paratext in paratextlist:
            newparatextlist.append(paratext.encode("utf-8"))
        return '\n\n'.join(newparatextlist)
    elif filename[-4:] == ".odt":
        cmd = ['odt2txt', filename]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        return stdout.decode('ascii', 'ignore')
    '''elif filename[-4:] == ".pdf":
		return convert_pdf_to_txt(file_path)'''



data_dir = 'resumes/'
output_dir = 'output/'
for a, b, c  in os.walk(data_dir):
    pass
for i in c:
    text = str(i)
    print 'opening ',text
    if 'a' in text:
        dot_index = text.index('.')
        original_name = text[:dot_index]
        ext_name = text[dot_index:]
        file_path = data_dir + text
        output_path = output_dir + original_name + '.txt'
        if ext_name == '.pdf':
            content_text = convert_pdf_to_txt(file_path)
        elif ext_name == '.doc':
            content_text = document_to_text(file_path)
        elif ext_name == '.docx':
            content_text = document_to_text(file_path)
        elif ext_name == '.odt':
            content_text = document_to_text(file_path)
        else:
            print 'left', text
        file1 = open(output_path,'w')
        file1.write(content_text)
        file1.close()
        print 'processed ',original_name