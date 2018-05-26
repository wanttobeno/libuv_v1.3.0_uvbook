import os
import sys

path=os.path.dirname(os.path.realpath(__file__))
alllist=os.listdir(path)
for i in alllist:
    destPath= path+"\\"+i
    if os.path.isdir(destPath):
        for fileIn in os.listdir(destPath):
            if("CMakeLists" in fileIn):
                delfile=destPath+"\\"+fileIn
                print "Del "+delfile
                os.remove(delfile) 
    else:
        print(destPath+" Is not a dir")
     