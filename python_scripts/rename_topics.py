#http://stackoverflow.com/questions/23203990/using-a-python-program-to-rename-all-xml-files-within-a-linux-directory

import xml.etree.ElementTree as ET


files = glob.glob('dir/*.dita')
tree = ET.parse('target.dita')
root = tree.getroot()
