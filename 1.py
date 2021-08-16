import os
import shutil
def allFilePath(rootPath,allFIleList):
    fileList = os.listdir(rootPath)
    for temp in fileList:
        if os.path.isfile(os.path.join(rootPath,temp)):
            allFIleList.append(os.path.join(rootPath,temp))
        else:
            allFilePath(os.path.join(rootPath,temp),allFIleList)

rootfile = r"./"

fileList =[]
allFilePath(rootfile,fileList)
for file in fileList:
    if file.endswith(".txt"):
        print(file)
