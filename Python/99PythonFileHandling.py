
#File Handling using pathlib ,shutil and os from system
#Each different way has been commented differently
import os
from os import system
###import shutil
#from pathlib import Path
##path("data").mkdir(exist_ok=True) ## make a directory
#if not os.path.exists("data")
#    os.mkdir("data")## make a directory
### shutil.move(file,"data")## move files to a new directory
#### shutil.copy2(file,"data")## copy files with meta data

##### os.remove("filename") ## remove a file
##### os.rmdir("data") ## remove a directory ,errors if not empty
##### shutil.rmtree("data") ## removes a directory with files in it

system("cls")## clear screen
print(os.getcwd())## get current directory
os.chdir('/MyStuff2022')## change to this directory

for file in os.listdir(): ## for each file in the directory
    if file == '.DS_Store':
        continue
    name,ext = os.path.splitext(file) ## split name and extension
    splitted = name.split("-")
    splitted = [s.strip() for s in splitted] ## remove spaces at beginning if name
    #print(splitted)
    new_name = f"{splitted[0]}{ext}"
    print(new_name)
#os.rename(file,new_name) ## rename a file

