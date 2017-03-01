import os, sys, string, re
from PyPDF2 import PdfFileWriter, PdfFileReader

pdffile = ("C:\\Users\\areilly\\Desktop\\PDF_OUTPUT\\S4010-0006_AR+++.pdf")
keywordfile = ("searchwords.txt")  

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
    content = " ".join(content.replace(u"\xa0", u" ").strip().split())
    return content

#http://conjugateprior.org/software/ca-in-python/


#this bit isn't working. i need to lowercase the text (a.lower), and then pass on the scraped text...
# store the PDF scrape
a = getPDFContent('')
text = (a.lower()) # lowercase the text

#read the keywords
a = open(keywordfile)
lines = a.readlines()
a.close()

cat = {}
scores = {}

# a default category for simple word lists
current_category = "Default"
scores[current_category] = 0

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
