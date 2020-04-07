'''
 使用python代码统计一个文件夹中所有文件的总大小
'''
import os
def dir_file_size(path): 
    if os.path.isdir(path): 
        file_size = 0 
        dir_list = os.listdir(path)
        for dir_name in dir_list: 
            file_path = os.path.join(path,dir_name) 
            if os.path.isfile(dir_name): 
                file_size += os.path.getsize(file_path) 
            else: 
                ret = dir_file_size(file_path) 
                file_size += ret 
                return file_size 
    elif os.path.isfile(path): 
        return os.path.getsize(path) 
    else:print('找不到%s文件'%path) 

path="D:/git_workspace"
size=dir_file_size(path)
print(size)
