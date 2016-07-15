# This module takes in dir1 and dir2 and creates the folder structure located in dir1 in dir2
import os


def duplicate(dir1,dir2):

    if dir1 != dir2:
        for dirpath, dirnames, filenames in os.walk(dir1):
            os.mkdir(os.path.join(dir2, dirpath[1 + len(dir1):]))