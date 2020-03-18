# -*- coding: utf-8 -*-

import os
#对所有文件以数字递增的方式重命名
def file_rename():
    i = 0
    #需要重命名的文件绝对路径
    path = r".\80songs\75songs"
    filelist = os.listdir(path)  
    #遍历所有文件
    for files in filelist:   
        Olddir = os.path.join(path, files)    
        if os.path.isdir(Olddir):       
                continue
        filename = os.path.splitext(files)[0]     
        filetype = os.path.splitext(files)[1]         
        Newdir = os.path.join(path, str(i)+filetype)   
        os.rename(Olddir, Newdir)   
        i+=1
    return True

if __name__ == '__main__':
    file_rename()
