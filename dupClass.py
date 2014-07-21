#!/usr/bin/python
import re

# Find duplicate class names
# 
# Start:        July 17, 2014
# Completed:    ---
#
# Notes:        ---

filename        = 'css/testfile.txt'
outFile         = 'css/dupOut.txt'

pattern         = '\.-?[_a-zA-Z]+[_a-zA-Z0-9-]*'
startPattern    = '{'
stopPattern     = '}'
outPattern      = []
compareList     = []
inStatement     = False

#parse css file to extract class names
with open(filename) as f:
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

# quick fix instead of using enumerate because of overflow in conditional
count = 0
for elem in outPattern:
    print count
    if count == 0:
        compareList.append(elem)
        count =+ 1

    for compid,compElem in enumerate(compareList):
        if compareList[compid] == elem:
            print 'found dup %s' % elem
            compareBool = True
            break
        else:
            continue
    if not compareBool:
        compareList.append(elem)
        count =+ 1
    else:
        continue

# for count,elem in enumerate(outPattern):
#     print count
#     if count == 0:
#         compareList.append(elem)
#     elif compareList[count-1] == elem:
#         continue
#     else:
#         compareList.append(elem)

print compareList

with open(outFile, 'w') as f:
    f.seek(0)
    f.writelines(compareList)
