import os
from datetime import datetime
import pickle
# Tạo file 1GB
filename = "virtual_disk.img"
with open(filename, "wb") as f:
    f.seek(1024*1024*1024)
    f.write(b"\0")

# Di chuyển vào thư mục chứa file ảo
os.chdir(os.path.dirname(os.path.abspath(__file__)))
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

# Tạo thư mục gốc
root_folder = Folder("root", "\\", datetime.now())
with open("virtual_disk.img", "wb") as f:
    # Viết cây thư mục vào đĩa ảo
    f.write(pickle.dumps(root_folder))
    f.seek(1024*1024*1024)
    f.write(b"\0")



