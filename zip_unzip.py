import zipfile # it is a python standerd library
my_zip = zipfile.ZipFile('files.zip', 'w')
# for creating zip file

my_zip.write('text.txt')# we are making here a text file.
my_zip.write('thumbnail.png')# creating png file

# for closing file
my_zip.close()

# can create this using "with" and "as"
with zipfile.ZipFile('filess.zip', 'w', compression=zipfile.ZIP_DEFLATED ) as my_zipp:# we used this for compression of our zip file.
    my_zipp.write("text_file.txt")
    my_zipp.write("thumb.jpg")
    # this was a second method for us.


#we cam unzip the file using extractall fx
with zipfile.ZipFile('filess.zip', 'r') as my_zipp:
    print(my_zipp.namelist())# this is for listing the name of items which we are going to unzip.
    my_zipp.extractall("naem of the file director where we want to extract")#this for extraction.
    # for extracting a specific file we use "Extract" fx instead of "extractall".
    my_zipp.extract('name fo the file with extension = file.png')