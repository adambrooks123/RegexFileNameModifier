########################
# 用于修改文件名的程序     #
# RegexFileNameModifier #
#     12/3/2021        #
########################

# V1.1 Add detection for unmatched cases, and job summary

import os
import re
from shutil import copy2

# 如需直接修改，将此处修改为 True
# 危险操作，慎重/ CAREFUL 
# Change this variable to True if you want to change the files at the dictinary
changeDirectly = False

# 此处填写文件所在的文件夹位置
# The files dictionary 
path = '...'

# 此处填写需要复制到的文件夹位置
# The destionation dictionary 
des_path = '...'

if not os.path.exists(des_path):
    os.makedirs(des_path)

fileList = os.listdir(path)

total = 0
success_count = 0
err_file = []

for fileName in fileList:
    oldName = path + os.sep + fileName
    total += 1
    
    # 命名规则，按需修改
    # Regex Rules, Modify this part if needed 
    # 此处例：修改'XX--XX20XX-XX.pdf' 为 ‘XX--XX公司20XX.pdf’
    # Example: Change 'XX--XX20XX-XX.pdf' to ‘XX--XX公司20XX.pdf’

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

# 完成情况及错误报告
# Job Summary & Error Report
print("=========SUMMARY===========")
print('{} files has been processed. {} name changed; {} unchanged. '.format(total, success_count, len(err_file)))
print("ERROR FILE NAMES:")
for names in err_file:
    print(names)
