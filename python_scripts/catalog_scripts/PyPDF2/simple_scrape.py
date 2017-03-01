import os, sys, string, re
from PyPDF2 import PdfFileWriter, PdfFileReader

pdffile = ("//tycofs.com/gbs/ResearchDevelopment/TechComms/AidanWork_Network/S4010-0006_AR+++.pdf")
keywordfile = ("searchwords.txt")  
#pdffile = sys.argv[1]
#keywordfile = sys.argv[2]



#http://stackoverflow.com/questions/25089033/how-to-search-keywords-in-400-pdf-files

def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = PdfFileReader(file(pdffile, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", u" ").strip().split())
    return content
a = getPDFContent('')
text = (a.lower())
print text
