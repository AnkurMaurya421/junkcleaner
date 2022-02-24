import os
from pathlib import Path
from tkinter import messagebox
import math
import shutil
import time
home = str(Path.home())      # get home directory
homedir=os.listdir(home)     #get directories inside home directory
filesizedictionary={}        #dictionary to store size of file
filelocationdictionary={}    #dictionary to store location of file
accesstimedictionary={}      #dictionary to store last access time of file



def convert_size(size_bytes):# covert size in bytes to readable format
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])


def traversedirectory(directory):      #traverse directory to store file or folder informations inside dictionary
    for j in os.listdir(directory):
        size=0
        Folderpath = (os.path.join(directory,j))
        if os.path.isdir(os.path.join(directory,j)):   # check if location is directory or file
            for path, dirs, files in os.walk(Folderpath):
                for f in files:
                    fp = os.path.join(path, f)
                    size += os.path.getsize(fp)
            size = convert_size(size)  # convert size
            if "MB" in str(size) or "GB" in str(size):        #only store those files whose size is either in MB or GB
                filelocationdictionary[j]=os.path.join(directory,j)
                filesizedictionary[j]=str(size)
                accesstimedictionary[j]=time.ctime(os.stat(os.path.join(directory,j)).st_mtime)
        else:
            size = os.path.getsize(os.path.join(directory,j))
            size=convert_size(size)
            if "MB" in str(size) or "GB" in str(size):
                filelocationdictionary[j] = os.path.join(directory, j)                                   #store location of file
                filesizedictionary[j] = str(size)                                                      #store size of file
                accesstimedictionary[j] = time.ctime(os.stat(os.path.join(directory, j)).st_mtime)       #store last access time of file
foldertobecheked={"Desktop","Downloads","Pictures","Videos","Documents","Music"}                    #only folders to be checked


for directory in homedir:                                                                              #traverse in home directory
    if os.path.isdir((os.path.join(home,directory))) and (directory in foldertobecheked):              #check if given location is folder and it exists in foldertobechecked
        traversedirectory((os.path.join(home,directory)))                                              # if true then traverse that folder

def returndic():
    return filesizedictionary,filelocationdictionary,accesstimedictionary           # return these three dictionaries to gui program

def deletefile(location):         #function to delete file or folder
    try:
        import os
        if os.path.isdir(location):   #if location is folder
            shutil.rmtree(location)
        else:                                 #if location is file
            if os.path.exists(location):
                os.remove(location)
            else:
                messagebox.showerror("showerror"," already deleted ")
    except:
        messagebox.showerror("showerror", " error occured")

