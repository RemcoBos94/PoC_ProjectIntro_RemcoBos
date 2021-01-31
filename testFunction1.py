import numpy as np
import pandas as pd
import openpyxl
import glob
import os
import array as arr
import shutil
from re import search



# input from GUI

input1 = "Remco"
folderPath = "C:/Excel/searchFolder"
folderdestination = "C:/Excel/destinationFolder"

# code itself



os.chdir(folderPath)
FileList = glob.glob('**/*.xlsx', recursive=True)


y = len(FileList)
print(FileList)

out = arr.array('h')



for x in range(y):
    
    counter = 0
    xls = pd.ExcelFile(FileList[x])
    sheetNames = xls.sheet_names
    l = len(sheetNames)

    for i in range(l):

        df = pd.read_excel(FileList[x], sheet_name=sheetNames[i])
        filteredData1= df[df.apply(lambda row: row.astype(str).str.contains(input1).any(), axis=1)]
        if not filteredData1.empty:
            counter = counter + 1

    if counter == 0:
        out.append(0)
    else:
        out.append(1)
        




print(FileList)
print(out)
print(FileList[0])
print(out[0])

for x in range(y):
    print(x)


z = 0

for x in range(y):
    if out[x] == 0:
        del FileList[z]
    else:
        z = z + 1



# output => prints list with excel files that consist the word

n = len(FileList)
print(n)


for i in range(n):
    filei = FileList[i]
    substring = "\\"
    if filei.find(substring) != -1:
        filej = filei.replace("\\","/")
        split_string = filej.rsplit("/", 1)
        filename = split_string[1]
        original = r'' + folderPath + '/' + filej
        target = r'' + folderdestination + '/' + filename
        shutil.copyfile(original, target)
    else:
        original = r'' + folderPath + '/' + filei
        target = r'' + folderdestination + '/' + filei
        shutil.copyfile(original, target)
 
  

print(FileList)
print("Files have been copied to Destination Folder")
