# Lesson 2 : Getting Started with Images

### Goals: 

* Read an image, display it, save it
* **Functions:** `cv2.imread()`, `cv2.imshow()`, `cv2.imwrite()`

---

### Reading an Image:

- `cv2.imread(<image>, <1,0,-1>)

- 1: `cv2.IMREAD_COLOR`: loads a color image. Any transparency of image will be
  neglected. It is the default flag.
- 2: `cv2.IMREAD_GRAYSCALE`: Loads image in grayscale mode
- 3: `cv2.IMREAD_UNCHANGED`: Loads image as such including alpha channel

*Refer to part 1 of (ocvl2.py)[../practice/ocvl2.py]*

**NOTE:** Even if image path is incorrect, it will still render and no error
will be thrown. To check that path is correct, please be sure to try a print
statement.

---

### Display an Image:

The method `cv2.imshow()` will display the image in a window and automatically
fits that image in the window. 

The syntax is as follows: `cv2.imshow(<window name>, <image>)`

Generally includes the function: `cv2.waitKey()`

This is a keybind, it will wait for a keystroke. 0 means that it will wait
forever.

There are other options where if your image is too big, you can recreate into a
better size:
`cv2.namedWindow('image', cv2.WINDOW_NORMAL)`

Be sure to delete all windows when completed with: `cv2.destroyAllWindows()`

*Refer to part 2 of (ocvl2.py)[../practice/ocvl2.py]*

---

### Write an Image:

Use the function `cv2.imwrite()`

Syntax: `cv2.imwrite(<save location>, <image>)`

---

### Matplotlib:

Using pyplot : you can use

```{python}
plt.imshow(img, cmpa = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
```
