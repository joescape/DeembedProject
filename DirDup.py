import os

source_dir = "C:\Users\Joey\Desktop\TestDir\Dir1"
target_dir = "C:\Users\Joey\Desktop\TestDir\Dir2"

for dirpath, dirnames, filenames in os.walk (source_dir):
    os.mkdir (os.path.join (target_dir, dirpath[1+len (source_dir):]))

os.startfile (target_dir)