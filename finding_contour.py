import numpy as np
import cv2
import csv

#import image
img = cv2.imread('task2_2.png')

#make musk
def mask(image):
     #change the image from RGB to HSV
     image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
     #set threshold(min/max)
     grade_min = np.array([0, 1, 1], np.uint8)
     grade_max = np.array([179, 255, 255], np.uint8)
     #binarization by threshold
     threshold_img = cv2.inRange(image_hsv, grade_min, grade_max)
     threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)

     return(threshold_img)

#make mask image
img_mask = mask(img)
#make binary image
img_binary = cv2.cvtColor(img_mask, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_binary, 127, 255, cv2.THRESH_BINARY)

#detect the edge of image
_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#show number of contours
print("Number of contours = "+str(len(contours)))

#roop for length of contours
for i in range(len(contours)):
     #show the contours to check
     print(contours[i])
     #make csv file
     with open("xy.csv", 'w') as file:
          #roop for contours
          for j in contours[i]:
               #show coordinate
               print(j[0])

               writer = csv.writer(file, lineterminator = '\n')
               writer.writerows(j)

#draw edge line
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
#show original image
cv2.imshow('Image', img)
#show binary image
cv2.imshow('Image BINARY', img_binary)

cv2.waitKey(0)
cv2.destroyAllWindows()