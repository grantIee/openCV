import numpy as np
import cv2

# PART 1 # 

# Read an Image with No Flags (1)
img1 = cv2.imread('./images/ocvl2img.jpg')
# print(img1)

# Read an Image with Flag 2 (0)
img0 = cv2.imread('./images/ocvl2img.jpg', 0)
# print(img0)

# Read an Image with Flag 3 (-1)
img01 = cv2.imread('./images/ocvl2img.jpg', -1)
# print(img01)


# PART 2 #

# Open up the image in a window

'''
cv2.imshow('image', img01)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Open up the image in a reasonable window

'''
cv2.namedWindow('image0', cv2.WINDOW_NORMAL)
cv2.namedWindow('image01', cv2.WINDOW_NORMAL)
cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.imshow('image0', img0)
cv2.imshow('image01', img01)
cv2.imshow('image1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# Litle function to open and save

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img1)
k = cv2.waitKey(0)

# We can choose what key in particular

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('./images/ocvl2imgS.jpg', img1)
    cv2.destroyAllWindows()
