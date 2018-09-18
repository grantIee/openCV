# Lesson 4: Drawing Functions in OpenCV

### Goal:
- Learn to draw different geometric shapes with OpenCV

- **Functions**:
    - `cv2.line()`
    - `cv2.circle()`
    - `cv2.rectangle()`
    - `cv2.ellipse()`
    - `cv2.putText()`

- **General Arguments**:
    - `img`: the image you want to draw the shapes
    - `color`: the colorf ot eh shape
    - `thickness`: the thickness of the line or circle : for filling in use
      `-1`
    - `lineType`: Type of line used

------


### `cv2.line()`

- the image
- the starting point
- the ending point
- the color 
- the thickness of the line

### `cv2.circle()`

- the image
- the enter coordinate
- the **radius**
- the color
- the thickness

### `cv2.rectangle()`

- the image
- the **top-left**
- the **bottom-right**
- the color
- the thickness

### `cv2.ellipse()`

- the image
- the center
- (major axis length, minor axis length)
- angle
- start angle
- end angle
- color
- thickness
- linetype
- shift


