import sys
import os
from os import listdir
from os.path import isfile, isdir, join

mypath = sys.argv[1]
os.chdir(mypath)
if not os.path.exists('out'):
    os.mkdir('out')
os.chdir('..')

inDir = listdir(mypath)

for f in inDir:
    target = join(mypath, f)

    if isfile(target):
        f = open(target, "r")
        fileLines = f.readlines()
        splitPath = f.name.split('/')
        tmpNum = len(splitPath)
        splitPath.append(splitPath[tmpNum - 1])
        splitPath[tmpNum - 1] = 'out'
        path = '/'.join(splitPath)
        path = path.replace('.txt', '.real')
        
        with open(path, 'w') as writingFile:
            for f1 in fileLines:
                if f1 == fileLines[0]:
                    writingFile.write('.version 1.0\n')
                    writingFile.write('.numvar '+ f1)
                    varLine = ".variables"
                    for x in range(int(f1)):
                        varLine = varLine + " q" + str(x)
                    writingFile.write(varLine + '\n')
                    writingFile.write(varLine.replace('.variables', '.inputs') + '\n')
                    writingFile.write(varLine.replace('.variables', '.outputs') + '\n')
                    writingFile.write('.begin\n')
                else:
                    aLine = f1.split()
                    if aLine[1] == 'h' or aLine[1] == 'z':
                        writingFile.write(aLine[1] + '1 q' + aLine[2] + '\n')
                    elif aLine[1] == 'cz':
                        writingFile.write('z2 q' + aLine[2] + ' ' + aLine[3] + '\n')
                    elif aLine[1] == 'x_1_2':
                        writingFile.write('x1 q' + aLine[2] + '\n')
                    elif aLine[1] == 'y_1_2':
                        writingFile.write('y1 q' + aLine[2] + '\n')
                    elif aLine[1] == 't':
                        writingFile.write('q1:4 q' + aLine[2] + '\n')
            writingFile.close()
