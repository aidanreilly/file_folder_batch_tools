import os, sys, string, re
from PyPDF2 import PdfFileWriter, PdfFileReader

pdffile = ("//tycofs.com/gbs/ResearchDevelopment/TechComms/AidanWork_Network/S49AO-0001.pdf")
keywordfile = ("searchwords_simple_cut.txt")  

#uncomment to pass at cmd
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
    content = " ".join(content.replace(u"\xa0", u" ").strip().split()) #remove no-break space
    content = " ".join(content.replace(u"\xae", u" ").strip().split()) #remove register mark
    content = " ".join(content.replace(u"\ufb02", u" ").strip().split()) #remove LATIN SMALL LIGATURE FL
    content = " ".join(content.replace(u"\ufb01", u" ").strip().split()) #remove LATIN SMALL LIGATURE FI
    content = " ".join(content.replace(u"\xb5", u" ").strip().split()) #remove MICRO SIGN
    content = " ".join(content.replace(u"\xb0", u" ").strip().split()) #remove Degree SIGN
    content = " ".join(content.replace(u"\u0142", u" ").strip().split()) #remove LATIN SMALL LETTER L WITH STROKE
    content = " ".join(content.replace(u"\u0141", u" ").strip().split()) #remove LATIN BIG LETTER L WITH STROKE
    content = " ".join(content.replace(u"\xa9", u" ").strip().split()) #remove copyright
    content = " ".join(content.replace(u"\u0153", u" ").strip().split()) #remove LATIN SMALL LIGATURE OE
    content = " ".join(content.replace(u"\u2122", u" ").strip().split()) #remove TRADEMARK SIGN
    content = " ".join(content.replace(u"\xbe", u" ").strip().split()) #remove 3/4 fraction
    
    return content

#http://conjugateprior.org/software/ca-in-python/


#lowercase the text (a.lower), and then pass on the scraped text as an str object...
# store the PDF scrape
pdf_con = getPDFContent('')
r = str((pdf_con.lower())) # lowercase the text

#text needs to be a list variable
text = string.split(r)




#read the keywords
a = open(keywordfile)
lines = a.readlines()
a.close()

cat = {}
scores = {}

# a default category for simple word lists
# current_category = "Default"
# scores[current_category] = 0

# inhale the keyword dictionary
for line in lines:
    if line[0:2] == '>>':
        current_category = string.strip( line[2:] )
        scores[current_category] = 0
    else:
        line = line.strip()
        if len(line) > 0:
            pattern = re.compile(line, re.IGNORECASE)
            cat[pattern] = current_category

#examine the text
for token in text:
    for pattern in cat.keys():
        if pattern.match( token ):
            categ = cat[pattern]
            scores[categ] = scores[categ] + 1

#output score
for key in scores.keys():
    print key, ":", scores[key] 
