import os
import pickle
from datetime import datetime
class File:
    def __init__(self, name, path, created_time,content=None):
        self.name = name
        self.path = path
        self.created_time = created_time
        self.content = content

class Folder:
    def __init__(self, name, path, created_time, modified_time):
        self.name = name
        self.path = path
        self.created_time = created_time
        self.modified_time = modified_time
        self.contents = []
# Di chuyển vào thư mục chứa file ảo
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Đọc cây thư mục từ file ảo
with open("virtual_disk.img", "rb") as f:
    root_folder = pickle.load(f)
def tree(node, indent=0):
    if isinstance(node, Folder):
        print(" " * indent + "- " + node.name)
        for child in node.contents:
            tree(child, indent + 2)
    elif isinstance(node, File):
        print(" " * indent + "- " + node.name)

# Sử dụng hàm print_tree để in ra cây thư mục
tree(root_folder)

