import glob
#from skimage import io
file_list = glob.glob(r'D:\Juntran\OpenCV\\tiny_shoppee_train\BabyPants\*.*')
print(file_list)
my_list = []
for file in file_list:
    #im = io.imread(file)
    my_list.append(file)
    my_list1= file.split("\\")[-1]
    print(my_list1)