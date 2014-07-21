#!/usr/bin/python

# Find duplicate class names
# 
# Start:        July 17, 2014
# Completed:    ---
#
# Notes:        ---

# input files
baseFile        = 'css/baseOut.txt'
cmsFile         = 'css/cmsOut.txt'
homeFile        = 'css/homeOut.txt'

# output duplicate list
compiledDec     = 'css/decoratorDupList.txt'
outDupFile      = 'css/dupList.txt'

decoratorList   =   [
                    'css/baseOut.txt',
                    'css/cmsOut.txt',
                    'css/homeOut.txt'
                    ]

outPattern      = []
duplicateList   = []
dupBool         = False

for inFile in decoratorList:
    #parse css file to extract class names
    with open(inFile) as f:
        lines = f.readlines()

    for count,line in enumerate(lines):
        if count == 0:
            outPattern.append(line)
            continue

        for idx,elem in enumerate(outPattern):
            # print '\t %s' % idx
            if elem == line:
                # list of duplicates
                duplicateList.append(elem)
                dupBool = True
                break

        if not dupBool:
            outPattern.append(line)
        else:
            dupBool = False

    # compiled list of decorator class
    with open(compiledDec, 'w') as f:
        f.seek(0)
        f.writelines(outPattern)

    # list of duplicates
    with open(outDupFile, 'w') as f:
        f.seek(0)
        f.writelines(duplicateList)

