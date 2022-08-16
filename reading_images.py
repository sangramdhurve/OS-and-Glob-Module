# import required module
from pathlib import Path

# get the path/directory
folder_dir = 'D:\Juntran\OpenCV\\tiny_shoppee_train\BabyPants'

# iterate over files in
# that directory
images = Path(folder_dir).glob('*.jpg')
for i in images:
    print(i)
