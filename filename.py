#####################
# 用于修改文件名的程序 #
#     12/3/2021    #
####################

# V1.1 Add detection for unmatched cases, and job summary

import os
import re
from shutil import copy2

# 如需直接修改，将此处修改为 True
# 危险操作，慎重
changeDirectly = False

# 此处填写文件所在的文件夹位置
path = '/Users/adam/Desktop/C/filetest'

# 此处填写需要复制到的文件夹位置
des_path = '/Users/adam/Desktop/C/filetest2'

if not os.path.exists(des_path):
    os.makedirs(des_path)

fileList = os.listdir(path)

total = 0
success_count = 0
err_file = []

for fileName in fileList:
    oldName = path + os.sep + fileName
    total += 1
    
    # 命名规则
    result = re.search(r'[0-9]{4}', fileName)
    if result:
        startLoc, endLoc = result.span(0)
        nameLength = len(fileName)
        backPix = fileName[endLoc+1:nameLength-4]
        prePix = fileName[:len(backPix)]

        if backPix != prePix:
            newName = backPix + '--' +fileName[:startLoc] + '公司' + fileName[startLoc:endLoc] + '.pdf'
        else:
            newName = fileName[:startLoc] + '公司' + fileName[startLoc:endLoc] + '.pdf'

        if changeDirectly:
            os.rename(oldName, newName)
        else:
            copy2(oldName, os.path.join(des_path, newName))
        
        print(oldName, ' ------> ', newName)
        success_count += 1
    else:
        err_file.append(fileName)

    print(str(total) + 'File has Processed.')
    print('-'*25)

print("=========SUMMARY===========")
print('{} files has been processed. {} name changed; {} unchanged. '.format(total, success_count, len(err_file)))
print("ERROR FILE NAMES:")
for names in err_file:
    print(names)
