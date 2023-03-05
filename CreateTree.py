import os.path
from datetime import datetime
import pickle
import os
class File:
    def __init__(self, name, path, created_time,content=None):
        self.name = name
        self.path = path
        self.created_time = created_time
        self.content = content

class Folder:
    def __init__(self, name, path, created_time):
        self.name = name
        self.path = path
        self.created_time = created_time
        self.contents = []
#new_folder,\\new_folder
def CreateFoder(name,path,folder):
    documents_folder = Folder(name,path, datetime.now())
    folder.contents.append(documents_folder)
    return documents_folder

# "file.txt", "\\documents\\file.txt"
def CreateFile(name,path,folder):
    file_txt = File(name, path, datetime.now())
    folder.contents.append(file_txt)
    return file_txt

with open("virtual_disk.img", "rb") as f:
    root_folder = pickle.load(f)
s=CreateFoder("folder1","\\folder1",root_folder)
CreateFile("file1.txt","\\folder1\\file1.txt",s)
CreateFile("file2.txt","\\file1.txt",root_folder)
CreateFoder("folder2","\\folder1\\folder2",s)

b=CreateFoder("folderName","\\folderName",root_folder)
c=CreateFile("Masterfile.txt","\\folderName\\Masterfile.txt",b)



with open("virtual_disk.img", "wb") as f:
    pickle.dump(root_folder, f)
    f.seek(1024*1024*1024)
    f.write(b"\0")


