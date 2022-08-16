import cv2
import matplotlib.pyplot as plt
#import numpy
#we are using 1 for color image and 0 for gray scale image
img = cv2.imread("D:\Juntran\OpenCV", 1)
img_1 = cv2.imread("D:\Juntran\OpenCV",0)
print(img)
cv2.imshow("Image", img_1)
plt.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()
#print(type(img))#it would be numpy array


#print(img.shape)#(row, column, channels)