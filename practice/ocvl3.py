import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
#cap = cv.VideoCapture('./videos/cvl2vid.mp4')

# For Using Camera
'''
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Retrieve certain information
    # print(cap.get(0))

    # Change the frame
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH, 480)

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.color_bgr2gray)
    
    normal = cv.cvtColor(frame, 0)

    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
'''

# For using file of Video
'''
while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break
'''

# For saving a video 

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))


while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:
        frame = cv.flip(frame,0)

        # write the flipped frame
        out.write(frame)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        else:
            break
            
out.release()


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
