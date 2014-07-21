#!/usr/bin/python
import re

import dupClass
import sanitizedDup
import dupDecorator

# Find duplicate class names
# 
# Start:        July 17, 2014
# Completed:    ---
#
# Notes:        ---

compareList     =   [
                    'css/decoratorDupList.txt',
                    'css/bootOut.txt'
                    ]

outFile         = 'css/bootstrapDuplicates.txt'

outPattern      = []
duplicateList   = []
dupBool         = False

for inFile in compareList:
    #parse css file to extract class names
    with open(inFile) as f:
        lines = f.readlines()

    for count,line in enumerate(lines):
        if count == 0:
            outPattern.append(line)
            continue

        for idx,elem in enumerate(outPattern):
            if elem == line:
                # list of duplicates
                duplicateList.append(elem)
                dupBool = True
                break

        if not dupBool:
            outPattern.append(line)
        else:
            dupBool = False

    with open(outFile, 'w') as f:
        f.seek(0)
        f.writelines(duplicateList)
