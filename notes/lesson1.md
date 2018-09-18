# Lesson 1 - The Basic Images Container

### Main Points:

- Learn how OpenCV stores and handles images
- Mat
- Storing Methods
- Creating a Mat Object
- Output Formatting
- Output of other Common Items


---

### Mat

OpenCV was born in 2001

Originally made in C, needed for all memory and data to be managed manually

**The Mat Object**
- Class with two data parts: 
    - the matrix header 
        - size of the matrix
        - the method used for storing
        - at which address the matrix is stored
    - pointer to the matrix

- Matrix header size is constant
- OpenCV needs to work with images, so lets try to make sure that the images
  are not copied over gazillion times
- Assignment operator and the copy constructor only copies the header
- The underlying matrix of an image may be copied using the `clone()` and
  `copyTo()`

---

### Storing Methods

Storing pixel values:

- RGB : the most common one : most similar to our vision
- HSV and HLS : based on hue, saturation, value/luminance : more natural way
  for us to describe colors
- YCrCb : popular JPEG image format
- CIE L\*a\*b\* : uniform color space, which comes handy when you need to
  measure the distance of a given color 

