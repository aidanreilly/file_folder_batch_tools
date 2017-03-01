#Insert metadata into docx from csv
#requires pywin32, run in python 3
#could also be modifed to run on other files
#make sure acrobat and word are closed

import csv
from docx import Document
import os
import sys
import time

csv_path = "datasheet_metadata_uplift.csv"

#set up the lists that will be used to hold csv values 
filename = []
title = []
keywords = []

#sets up the csv file, and parses "columns" to one of three lists: filename, title, keywords
f = open(csv_path)
csv_file = csv.reader(f)

#chops up csv into [] lists
for row in csv_file:
    filename.append(row[0])
    title.append(row[1])
    keywords.append(row[2])

#get the number of lines in the csv, and thus the files that need updating
file = open(csv_path)
num_lines = len(file.readlines())

#do the updates on every filename in the list
i = 0
while i < num_lines:
    if i < num_lines:
        #update the docx files, one for each csv file entry
        document = Document(filename[i])
        core_properties = document.core_properties
        core_properties.keywords = (keywords[i])
        core_properties.title = (title[i])
        core_properties.subject = ("Simplex Fire Protection Technical Product Datasheet")
        core_properties.comments = (" ")
        document.save(filename[i])
        i+=1

print ("finished!")





