import os
import sys
import shutil

path=os.path.dirname(os.path.realpath(__file__))
alllist=os.listdir(path)
file = u"CMakeLists.txt"
srcFile= path+"\\"+file
for i in alllist:
    newname= path+"\\"+i
    if os.path.isdir(newname):
        newname= newname+"\\"+file
        #print(srcFile)
        #print(newname)
        shutil.copyfile(srcFile,newname)
    else:
        #print(srcFile)
        print(newname+" Is not a dir")
     