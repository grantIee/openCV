import numpy as np
import cv2 as cv

# Create Background
img = np.zeros((512,512,3), np.uint8)

cv.circle(img,(256,128),70,(0,0,255), -1)
cv.circle(img,(326,249),70,(255,0,0), -1)
cv.circle(img,(186,249),70,(0,255,0), -1)
cv.circle(img,(256,128),17,(0,0,0), -1)
cv.circle(img,(186,249),17,(0,0,0), -1)
cv.circle(img,(326,249),17,(0,0,0), -1)

cv.ellipse(img,(256,128),(70,70),60,0,60,0,-1)
cv.ellipse(img,(326,249),(70,70),240,0,60,0,-1)
cv.ellipse(img,(186,249),(70,70),300,0,60,0,-1)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10,420),font,4,(255,255,255),9,cv.LINE_AA)


cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
