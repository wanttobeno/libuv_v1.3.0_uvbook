import os
import sys
import string

path=os.path.dirname(os.path.realpath(__file__))
alllist=os.listdir(path)
file = u"CMakeLists.in"
destfile = u"CMakeLists.txt"
srcFile= path+"\\"+file
# read file
f = open(srcFile,'r')
f_data = f.read()
#print(f_data)
for i in alllist:
    destPath= path+"\\"+i
    if os.path.isdir(destPath):
        newname= destPath+"\\"+destfile
        #print(srcFile)
        #print(newname)
        fwrite=open(newname,'wb')
        fwrite.write('############ Gen By Python Script ############\n\n')
        fwrite.write('project('+i+')\n')

        fwrite.write('add_executable (${PROJECT_NAME} ')
        for fileIn in os.listdir(destPath):
            fileLower=fileIn.lower()
            if(".c" in fileLower):
                #print fileIn
                fwrite.write(fileIn+" ")
            elif(".cc" in fileLower):
                #print fileIn
                fwrite.write(fileIn+" ")
            elif(".cpp" in fileLower):
                #print fileIn
                fwrite.write(fileIn+" ")
            #print fileIn
    
        fwrite.write(')\n\n')
        fwrite.write('############ Gen By Python Script ############\n\n')
        fwrite.write(f_data)
    else:
        #print(srcFile)
        print(newname+" Is not a dir")
     