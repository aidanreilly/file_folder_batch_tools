#python 3, 32bit
import re
import glob
import os
import shutil
import xml.etree.ElementTree as ET

# command line arguments - we could use this on the command line
# dita_folder = sys.argv[1]

#open and process the dita files:
for filename in glob.glob('*.dita'):
        #put file in memory
        #dita_file=open(filename,'r',encoding='UTF-8')
        tree = ET.parse(filename)
        root = tree.getroot()
        #selects first title node contents 
        for title in root.findall('title'):
                print(title.text)
                #how do i put this in the filename?
                #how do i truncate?
                #this remove uppercase and spaces
                #os.rename(filename, filename.replace(" ", "-").lower())
                #needs a bit of work obvs. 

                
        
