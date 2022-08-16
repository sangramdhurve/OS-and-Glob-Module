import glob
 
rootdir = "D:\Juntran\OpenCV\\tiny_shoppee_train"
for path in glob.glob(f'{rootdir}/*/'):
    a = path.split("\\")[-2]
    print(a)
    