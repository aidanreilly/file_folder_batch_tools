#run in python 2.7
#run at command line to pipe to txt file
#if like i do, you have python 3 installed then: py -2.7 PDF_extractor.py > output.csv
#https://pythonhosted.org/PyPDF2/PdfFileReader.html

from pyPdf import PdfFileWriter, PdfFileReader
import os
import re

for fileName in os.listdir('.'):
    try:
        if fileName.lower()[-3:] != "pdf": continue
        input1 = PdfFileReader(file(fileName, "rb"))
        print fileName, '|', input1.getNumPages(), '|', input1.getDocumentInfo().title, '|', input1.getDocumentInfo().subject
    except:
        print 'error in this file:', fileName
