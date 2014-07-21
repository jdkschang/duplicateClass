#!/usr/bin/python
import re

# Find duplicate class names
# 
# Start:        July 17, 2014
# Completed:    ---
#
# Notes:        ---

inputList       =   [
                    'css/base.css',
                    'css/cms.css',
                    'css/homepage-wide.css',
                    'css/bootstrap.css',
                    ]

outputList       =   [
                    'css/output/baseOut.txt',
                    'css/output/cmsOut.txt',
                    'css/output/homeOut.txt',
                    'css/output/bootOut.txt',
                    ]

pattern         = '\.-?[_a-zA-Z]+[_a-zA-Z0-9-]*'
startPattern    = '{'
stopPattern     = '}'

inStatement     = False

for idx,inFile in enumerate(inputList):
    outPattern          = []
    #parse css file to extract class names
    with open(inFile) as f:
        lines = f.readlines()

    for line in lines:
        match           = re.findall(pattern, line)
        breakStartMatch = re.search(startPattern, line)
        breakStopMatch  = re.search(stopPattern, line)

        # bracketed statement on one line
        if breakStartMatch and breakStopMatch:
            preTest = str(line).split('{')[0].strip() + '\n'
            sufTest = str(line).split('}')[1].strip() + '\n'

            outPattern.append(preTest)
            outPattern.append(sufTest)
            continue

        elif match and not inStatement:
            new_line = '\n'.join(map(str, match)).strip() + '\n'
            outPattern.append(new_line)

        # parse through until stop Pattern
        if breakStartMatch:
            inStatement = True
        elif breakStopMatch:
            inStatement = False

    with open(outputList[idx], 'w') as f:
        f.seek(0)
        f.writelines(outPattern)
