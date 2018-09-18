# Lesson 3: Getting Started with Videos

### Goals:

* Read video, display video, save video
* Capture from Camera and display it
* **Functions:** `cv2.VideoCapture()`, `cv2.VideoWriter()`

---

### Capture Video from Camera

- Always begin with a **VideoCapture** object
- Arguments: *device index*, *name of the video file*
    - Device Index: Which camera will be used

- Keep in mind that the statement: `ret, frame = capt.read()`
    - `ret`: obtaining the return value from getting the camera frame
      (true/false)
    - `frame`: gets the next frame in the camera

---

### Playing a Video From File

- Same idea as capturing a video from the camera, except now you are changing
  the input source to a specific file

---

### Saving a Video

- For images we could just use `cv2.imwrite()`
- For movies there is a longer process required:

    - We have to use a **VideoWriter** object. 
    - **Arguments**: 
        - Output file name
        - Specify the **FourCC** code
        - Number the frames per second
        - Frame size
        - **isColor** flag
    

    - **FourCC**: 

        - DIVX, XVID, MJPG, X264, WMV1, WMV2
        - General Format: `cv2.VideoWriter_fourcc(*'MJPG')`

