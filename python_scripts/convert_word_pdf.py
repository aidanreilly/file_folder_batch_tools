# Convert doc files to pdf
# requires pywin32, run in 32bit python
# could also be modifed to run on docx, other files
# for other files: https://msdn.microsoft.com/en-us/library/office/ff839952.aspx

import glob
import os
from win32com import client

folder = "."
file_type = "doc"

for filename in glob.iglob("./**/*.doc", recursive=True):

    try:
        out_name = filename.replace(file_type, r"pdf")
        in_file = os.path.abspath(folder + "\\" + filename)
        out_file = os.path.abspath(folder + "\\" + out_name)
        word = client.Dispatch("Word.Application")
        doc = word.Documents.Open(in_file)
        print ("Exporting", out_file)
        doc.SaveAs(out_file, FileFormat=17)
        doc.Close()
        
        
    except (Exception, e):
        print ("Soemthing went wrong dingus")
word.Quit()


