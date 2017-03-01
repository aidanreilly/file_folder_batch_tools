 #!/usr/bin/python
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

'''
Desired output:
 { "name" : "ABC", "parent":"DEF", "relation": "ghi", "size": 1 },
 { "name" : "DEF", "parent":"null", "relation": "null", "size": 3 },
 { "name" : "new_name", "parent":"ABC", "relation": "rel", "size": 2 },
 { "name" : "new_name2", "parent":"ABC", "relation": "foo", "size": 2 },
 { "name" : "Foo", "parent":"DEF", "relation": "rel", "size": 5 },
'''


# Creating an empty list that will contain the already traversed paths
donePaths = []
count = 0
#path = ("C:\\Users\\acollins\\Documents\Stretch\\JCI_content_visualisation\\mock_dir_tree\\JCI")
#rm_path = ("C:\\Users\\acollins\\Documents\Stretch\\JCI_content_visualisation\\mock_dir_tree\\")
path = ("C:\\Users\\areilly\\Desktop\\PDF_OUTPUT\\") 
rm_path = ("C:\\Users\\areilly\\Desktop\\")
out_file = ("out_file.txt")

f = open(out_file,'w')
f2 = open('year.txt','w')
f3 = open('tool.txt','w')

f.write('{"name" : "JC_PDF", "parent" : "null"},')
f.write('\n')
num_pages = 10
for paths,dirs,files in os.walk(path):
        if paths not in donePaths:
                count = paths.count('\\')
                count = count -7
                if files:
                        for ele1 in files:
                                if(ele1.find('.pdf')>0):
                                        filePath1 = os.path.join(paths, ele1)
                                        filePath = filePath1.replace(rm_path,"")
                                        #split
                                        splits = filePath.split("\\")
                                        #extract page count
                                        inputStream=file(str(filePath1), "rb")
                                        #input_PDF = PdfFileReader(str(filePath1))
                                        input_PDF = PdfFileReader(inputStream)
                                        num_pages = str(input_PDF.getNumPages())
                                        try:
                                                q = input_PDF.getXmpMetadata()
                                                year_val = str.split(str(q.xmp_createDate),'-')
                                                tool_val = str(q.xmp_creatorTool)
                                        except:
                                                year_val[0] = 2016

                                                
                                        inputStream.close()
                                        f2.write(str(year_val[0]) + '\n')
                                        f3.write(tool_val + '\n')
                                        f.write('{"name" : "' + splits[len(splits)-1] + '", "parent" : "' + splits[len(splits)-2] +  '", "size" : "' +   str(num_pages) + '", "year" : "' + str(year_val[0])  + '", "tool" : "' + tool_val + '"},')
                                        f.write('\n')
                                        #print splits
                                        #print len(splits)
                                        
                if dirs:
                        for ele2 in dirs:
                                absPath = os.path.join(paths,ele2)
                                absPath = absPath.replace(rm_path,"")
                                splits = absPath.split("\\")
                                #print splits
                                #print len(splits)
                                f.write('{"name" : "' + splits[len(splits)-1] + '", "parent" : "' + splits[len(splits)-2] + '"},')
                                f.write('\n')

f.close()
f2.close()
f3.close()
