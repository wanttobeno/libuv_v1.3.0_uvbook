import os
import sys

path=os.path.dirname(os.path.realpath(__file__))
alllist=os.listdir(path)
for i in alllist:
    fulname= path+"\\"+i
    if os.path.isdir(fulname):
        #print(srcFile)
        #print(i)
        print "add_subdirectory(code/"+i+")"
        