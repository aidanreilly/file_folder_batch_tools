import sys, string, re

# command line arguments
dictfile = 'egdict.txt'
textfile = 'idtext.txt'

a = open(textfile)
text = string.split( a.read() ) # lowercase the text
a.close()

a = open(dictfile)
lines = a.readlines()
a.close()

dic = {}
scores = {}

# a default category for simple word lists
current_category = "Default"
scores[current_category] = 0

# inhale the dictionary
for line in lines:
    if line[0:2] == '>>':
        current_category = string.strip( line[2:] )
        scores[current_category] = 0
    else:
        line = line.strip()
        if len(line) > 0:
            pattern = re.compile(line, re.IGNORECASE)
            dic[pattern] = current_category

# examine the text
for token in text:
    for pattern in dic.keys():
        if pattern.match( token ):
            categ = dic[pattern]
            scores[categ] = scores[categ] + 1

for key in scores.keys():
    print key, ":", scores[key]
