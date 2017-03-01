#http://www.computerhope.com/forum/index.php?topic=85285.0

import os,glob,sys,re
folder=sys.argv[1]
os.chdir(folder)
pattern = re.compile(".*<PATH_XML>(.*?)</PATH_XML>.*",re.DOTALL|re.MULTILINE|re.IGNORECASE)
for files in glob.glob("Recovered*"):
    data=open(files).read()
    if pattern.search(data):
        newfilename = pattern.findall(data)[0].split("\\")[2] #get the new file name
        try:
            os.rename(files,os.path.join(folder,newfilename+".xml"))
        except Exception,e:
            print e
        else:
            print "%s renamed to %s.xml" %(files,newfilename)
