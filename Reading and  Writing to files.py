# file objects
f = open('data.txt', 'r')# onening file
# for reading 'r', writing 'w', append 'a', reading end wirte file 'r+'
print(f.name)# f.name will give us name of file
print(f.mode)# it will give us mode of the fx.
f.close()
# contex management
# befile of contex managers we don't have to close the file, it will close automatically.
with open('data.txt','r') as f:
    size_to_read = 100#optional
    f_contents = f.read(size_to_read)#for reading the file. it takes argument how many character you want inside the function.
    f.readlines()# for raading in one line (list of file).
    f.readline()# for single first line.
    while len(f_contents) > 0:
        print(f_contents, end= ' ')# if there will be some character it will give us otherwise no.
        f_contents = f.read(size_to_read)
print(f.closed)# it will return True or False.

# we iterate all line
for line in f:
    print(line, end=' ')
# for check no of file it will return last no. of file.
print(f.tell())


#PART..........2
# writing the file.
with open('data2.txt') as f:
    f.write('write the content what you want to write in your file.')
    f.seek(0) # it will overwrite the content which allready exist in the file.
    f.write('the the content what you want to overwrite in file. using index we can write in perticuler position')


# good fx for reading and wrinting file in single code.
with open('data.txt', 'r') as rf:
    with open('data_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# for images we have to use binary mode "rb" and "wb"
with open('data.jpg', 'rb') as rf:
    with open('data_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


#thankk you for this code
#if you want any type of code and library please direct DM to me I'll solve that for you, thank you.