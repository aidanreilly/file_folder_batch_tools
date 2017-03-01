#untested - see https://groups.google.com/forum/#!topic/python-docx/0sX7DstKgto

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.text.run import Run

# Configure
style = 'Figure'              # Can be 'Figure', 'Table' or 'Equation'
num = 1

# Initialize
d = Document()
p = d.add_paragraph()

# Insert caption
elem = p._element
r = OxmlElement('w:r')
elem.append(r)
Run(r, p).text = style + ' '

# Insert caption number   
pCaption = OxmlElement('w:fldSimple')
pCaption.set(qn('w:instr'), r' SEQ {style} \* ARABIC '.format(style=style))
elem.append(pCaption)
    
r = OxmlElement('w:r')
pCaption.append(r)
    
rPr = OxmlElement('w:rPr')
r.append(rPr)
    
rPr.append(OxmlElement('w:noProof'))
    
Run(r, p).text = str(num)
