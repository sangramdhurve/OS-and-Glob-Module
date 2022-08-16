from zipfile import ZipFile #this library we use for zip and unzip our file

# we are using here zipfile function and giving the zipped file path and reading with "r".
unzip= ZipFile("D:\Juntran\OpenCV\\tiny_shoppee_train.zip", "r")
# we are using here extractall fx for extraction of all folders & files inside that and
# giving the path for saving the file unziped file.
unzip.extractall('D:\Juntran\OpenCV')
# we are closing here our file.
unzip.close()