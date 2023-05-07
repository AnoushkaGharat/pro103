import os
import shutil
from_dir="C:/Users/anous/Pro102"
to_dir = "C:/Users/anous/Downloads/organized"
list_of_files = os.listdir(from_dir)
print(list_of_files)

for files_name in list_of_files:
    name,ext = os.path.splitext(files_name)
    if ext == "": continue
    if ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + files_name
        path2 = to_dir + "/"+"Document_Files"+ ext
        path3 = to_dir + "/" + "Document_Files" + "/"+files_name
        if os.path.exists(path2):
            print("moving"+ files_name +"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+ files_name +"...")
            shutil.move(path1,path3)