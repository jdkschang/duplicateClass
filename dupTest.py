#!/usr/bin/python
import re
import dupClass

# Find duplicate class names
# 
# Start:        July 17, 2014
# Completed:    ---
#
# Notes:        ---

filename        = 'css/baseOut.txt'
outFile         = 'css/baseOut.txt'

outPattern      = []
duplicateList   = []
dupBool         = False

#parse css file to extract class names
with open(filename) as f:
    lines = f.readlines()

for count,line in enumerate(lines):
    if count == 0:
        outPattern.append(line)
        continue

    for idx,elem in enumerate(outPattern):
        # print '\t %s' % idx
        if elem == line:
            # print 'line value: %s' % line
            # print 'elem value: %s' % elem
            # print '\tduplicate FOUND'

            # list of duplicates
            duplicateList.append(elem)
            dupBool = True
            break

    if not dupBool:
        outPattern.append(line)
    else:
        dupBool = False

print duplicateList

with open(outFile, 'w') as f:
    f.seek(0)
    f.writelines(outPattern)
