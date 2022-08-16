import os
from datetime import datetime
#print(dir(os))# for printing all files available in operating system.
print(os.getcwd())# for printing current working directory
os.chdir('d:/Juntran/OpenCV/Os')# for changing the working direcory.
print(os.listdir())# for getting list of items in current directory.
os.mkdir('name of directory')# for making directory
os.makedirs()# deep directory we can create(subdir we can create).
os.rmdir("path of directory")# this is for not remove intermidiate directory.
os.removedirs("path")# it can remove intire directory.

os.rename('orignal file name', 'new name')# for rename file.

print(os.stat('name of file').st_size)# for getting size of file.
print(os.stat('demo.txt').st_mtime)# for knowing the modification time.
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp)(mod_time) # it will print date and time.
for dirpath, dirnames, filenames in os.walk('enter the path'):# it is a generator
    print('current path:', dirpath)
    print('directories:', dirnames)

    print('files:', filenames)
    print()# it will print out all the directories.


# environ
os.environ.get('Home environment')# this will give home directory invironment.


#how to create directory and file.
file_path = os.environ.get('Home') + 'text.txt'
print(file_path)

#update code for this
file_path = os.path.join(os.environ.get('Home'), 'text.txt')
print(file_path)


# creating new file
with open(file_path, 'w') as f:
    print(file_path)

os.path.basename('path')# it will give us only file name means basename of directory.
os.path.dirname("path")# it will only dirctory name excluding file name or basename.
print(os.path.split('path'))# it will give us (directory name and file name or basename)

# for verifing the path is existing or not
print(os.path.exists("path"))# it will return True or Flase.
# opt 1st       os.path.isdir("path")
# opt 2nd       os.path.isfile("path")

# for file extension
print(os.path.splitext("path"))

