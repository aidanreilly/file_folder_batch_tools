#runs in python 2.7
#run at command line to pipe to txt file
#if like i do, you have python 3 installed then: py -2.7 regex_scrape.py > output_PIDs.txt

import pyPdf
import re
import glob

#regex for PIDs
regex = r"([5][7][0-9]-[0-9]{3,4})"
# "([0-9][0-9][0-9][0-9]-[0-9]{3,4})" matches xxx-xxxx or xxx-xxx
# ([5][7][0-9]-[0-9]{3,4}) matches 57x-xxx or 57x-xxxx

#definition for extracting pdf text
def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content

for fileName in glob.iglob("*.pdf"):
    try:
        matches = re.findall(regex, getPDFContent(fileName).encode("ascii", "ignore"))
        print fileName, '|', (matches)

    except Exception, e:
        print "Something went wrong with ", fileName
