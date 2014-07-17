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
stopPattern     = '{|}'
outPattern      = []
inStatement     = False

#parse css file to extract class names
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    match           = re.findall(pattern, line)
    breakStartMatch = re.search(stopPattern, line)

    if match and not inStatement:
        new_line = '\n'.join(map(str, match)) + '\n'
        outPattern.append(new_line)

    # parse through until stop Pattern
    if breakStartMatch:
        inStatement = not inStatement
        continue

with open(outFile, 'w') as f:
    f.seek(0)
    f.writelines(outPattern)


