import base64
import os.path
from datetime import datetime
import pickle
import os
class Folder:
    def __init__(self, name, path, created_time):
        self.name = name
        self.path = path
        self.created_time = created_time
        self.contents = []

class File:
    def __init__(self, name, path, created_time,content=None):
        self.name = name
        self.path = path
        self.created_time = created_time
        self.content = content
def FindFileByName(name, folder):
    for item in folder.contents:
        if isinstance(item, Folder):
            result = FindFileByName(name, item)
            if result is not None:
                return result
        elif isinstance(item, File):
            if item.name == name:
                return item
    return None
# Hàm tạo thư mục con
def CreateFoder(name,path,folder):
    documents_folder = Folder(name,path, datetime.now())
    folder.contents.append(documents_folder)
    return documents_folder

def CreateFile(name,path,folder):
    file_txt = File(name, path, datetime.now())
    folder.contents.append(file_txt)
    return file_txt
def FindFolderByName(name, folder):
    if folder.name == name:
        return folder
    else:
        for subfolder in folder.contents:
            if isinstance(subfolder, Folder):
                result = FindFolderByName(name, subfolder)
                if result is not None:
                    return result
        return None
with open("virtual_disk.img", "rb") as f:
    root_folder = pickle.load(f)
folder_name="folder1"
folder = FindFolderByName(folder_name, root_folder)
s=FindFileByName("file1.txt", folder)
with open("test.html", "r") as f:
    text = f.read()
#Ma hóa
contentEncode = text.encode('utf-8')
encoded_b64 = base64.b64encode(contentEncode)
# s.content=encoded_b64
encoded_str = encoded_b64.decode('utf-8')
#Giải mã
contentDecode=encoded_str.encode('utf-8')
decoded_b64 = base64.b64decode(contentDecode)
decoded_str = decoded_b64.decode('utf-8')
print(decoded_str)