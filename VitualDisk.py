import os.path
from datetime import datetime
import pickle
import os

class File:
    def __init__(self, name, path, created_time, permissions):
        self.name = name
        self.path = path
        self.created_time = created_time
        self.permissions = permissions

class Folder:
    def __init__(self, name, path, created_time, permissions):
        self.name = name
        self.path = path
        self.created_time = created_time
        self.permissions = permissions
        self.contents = []

def CreateFolder(name, path, folder):
    documents_folder = Folder(name, path, datetime.now(), "rwxr-xr-x")
    folder.contents.append(documents_folder)
    return documents_folder

def CreateFile(name, path, folder):
    file_txt = File(name, path, datetime.now(), "rw-r--r--")
    folder.contents.append(file_txt)
    return file_txt

def CreateFolderAcc(nameacc, path, folder):
    CreateFolder(nameacc, path, folder)

# Open the virtual disk image file
with open("virtual_disk.img", "rb+") as f:
    # Load the root folder object
    root_folder = pickle.load(f)

    # Traverse the folder hierarchy to locate the Masterfile.txt object
    folder_name = "folderName"
    sub_folder_name = "abc"
    file_name = "Masterfile.txt"
    parent_folder = None
    sub_folder = None
    target_file = None
    for item in root_folder.contents:
        if isinstance(item, Folder) and item.name == folder_name:
            parent_folder = item
            for sub_item in parent_folder.contents:
                if isinstance(sub_item, Folder) and sub_item.name == sub_folder_name:
                    sub_folder = sub_item
                    for file_item in sub_folder.contents:
                        if isinstance(file_item, File) and file_item.name == file_name:
                            target_file = file_item

    # Write data to the Masterfile.txt object
    if target_file:
        with open("virtual_disk.img", "wb") as file_data:
            file_data.seek(target_file.path)
            file_data.write(b"New data to write")

    # Serialize the updated root folder object and write it back to the virtual disk image file
    pickle.dump(root_folder, f)
    file_size_before = os.path.getsize("virtual_disk.img")
    f.flush()
    os.fsync(f.fileno()) # Make sure all changes are written to disk
    file_size_after = os.path.getsize("virtual_disk.img")

    # Compare the sizes to see if the data was successfully written
    if file_size_after > file_size_before:
        print("Data was written successfully")
    else:
        print("Data was not written successfully")
    # Seek to the end of the virtual disk image file and write a null byte
    f.seek(1024*1024*1024)
    f.write(b"\0")
