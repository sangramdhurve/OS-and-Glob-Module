import os 
import glob
from pkgutil import extend_path

#for getting current working directory path.
file_path = os.getcwd()
print("this is file path name.......>", file_path)

#breaking into different components of the filepath
dir = os.path.dirname(file_path) #this gives the directory name.
extention_of_path = os.path.splitext(file_path)[1]#this will give us file extention name
print("extension name......>", extention_of_path)
filename = os.path.splitext(file_path)[0] # name of the file
print("finename of the file path...>", filename)


# joining different components
joincheckk = os.path.join(dir, filename, extention_of_path)# automaticall adds the / in the path
print(joincheckk)

listcheck = os.listdir(dir)# list of all the file name inside the directory

joincheck = os.path.join(dir, listcheck[0])
#for joining using the index

filesize = os.path.getsize(file_path)# size of the file in bytes

multiplefile = glob.glob(dir + "/*.xlsx")# gives multiple files through which can be iterate

for f in multiplefile:
    print("we can iterate like this..!!")