from zipfile import ZipFile
def UnZip(files):
    files1= ZipFile(files, "r")
    files1.extractall('D:\Juntran\OpenCV')
    files1.close()
    print("File has been successfuly Unzipped")

files = "D:\Juntran\OpenCV\\tiny_shoppee_train.zip"
UnZip(files)