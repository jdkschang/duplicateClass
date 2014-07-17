#!/usr/bin/python
import re

# Find duplicate class names
# 
# Start:        July 17, 2014
# Completed:    ---
#
# Notes:        ---

filename        = 'css/testfile.txt'
outFile         = 'css/outfile.txt'

pattern         = '\.-?[_a-zA-Z]+[_a-zA-Z0-9-]*'
startPattern    = '{'
stopPattern     = '}'
outPattern      = []
inStatement     = False

#parse css file to extract class names
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    match           = re.findall(pattern, line)
    breakStartMatch = re.search(startPattern, line)
    breakStopMatch  = re.search(stopPattern, line)

    # print 'line: %s' % line
    # print '\tmatch: %r' % match
    # print '\tinStatement: %s\n' % inStatement

    if breakStartMatch and breakStopMatch:
        preTest = str(line).split('{')[0]
        sufTest = str(line).split('}')[1]

        outPattern.append(preTest)
        outPattern.append(sufTest)
        continue

    elif match and not inStatement:
        new_line = '\n'.join(map(str, match)) + '\n'
        outPattern.append(new_line)

    # parse through until stop Pattern
    if breakStartMatch:
        inStatement = True
    elif breakStopMatch:
        inStatement = False

with open(outFile, 'w') as f:
    f.seek(0)
    f.writelines(outPattern)
