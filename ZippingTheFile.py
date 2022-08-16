from zipfile import ZipFile
ziping = ZipFile("D:\Juntran\OpenCV\\tiny_shoppee_train", "r")
for file in ziping:
        ziping.write(file)
        print("File has been zipped")