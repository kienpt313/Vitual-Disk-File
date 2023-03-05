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

# Hàm tạo thư mục con
def CreateFoder(name,path,folder):
    documents_folder = Folder(name,path, datetime.now())
    folder.contents.append(documents_folder)
    return documents_folder

def CreateFile(name,path,folder):
    file_txt = File(name, path, datetime.now())
    folder.contents.append(file_txt)
    return file_txt
#duyet cay de tim kiem
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

with open("thongtin.txt", "a+") as f:
    f.seek(0)
    lines = f.readlines()
    user = input("Enter username: ")
    password = input("Enter password: ")

    for line in lines:
        if user == line.split(":")[0].strip() and password==line.split(":")[1].strip():
            print("welcome")
            folder_name="folderName"
            new_folder_path = f"\\{folder_name}\\{user}"
            folder = FindFolderByName(folder_name, root_folder) #tim thu muc trong cay
            folderuser=FindFolderByName(user, folder) #tim thu muc trong file foldername
            if folderuser is None:
                CreateFoder(user,new_folder_path,folder)
            else:
                userfile=f"{user}${datetime.now()}.txt"
                new_userfile_path = f"\\{folder_name}\\{user}\\{userfile}"
                CreateFile(userfile,new_userfile_path,folderuser)
            break
        elif user == line.split(":")[0].strip() and password!=line.split(":")[1].strip():
            print("Sai mat khau")
            break
    else:  # Neu khong ton tai
        # them tai khoan mat khau vao file va tao thu muc
        f.write(f"{user}:{password}\n")
        print("User added successfully!")
        folder_name="folderName"
        new_folder_path = f"\\{folder_name}\\{user}"
        folder = FindFolderByName(folder_name, root_folder)
        CreateFoder(user,new_folder_path,folder)



with open("virtual_disk.img", "wb") as f:
    pickle.dump(root_folder, f)
    f.seek(1024*1024*1024)
    f.write(b"\0")       
