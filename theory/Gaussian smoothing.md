# Gaussian smoothing

### Image Smoothing using OpenCV Gaussian Blur

As in any other signals, images also can contain different types of noise, especially because of the source (camera sensor). Image Smoothing techniques help in reducing the noise. In OpenCV, image smoothing (also called blurring) could be done in many ways. In this tutorial, we shall learn using the Gaussian filter for image smoothing.

Gaussian filters have the properties of having no overshoot to a step function input while minimizing the rise and fall time. In terms of image processing, any sharp edges in images are smoothed while minimizing too much blurring.

### Syntax of cv2 gaussianblur function

OpenCV provides cv2.gaussianblur() function to apply Gaussian Smoothing on the input source image. Following is the syntax of GaussianBlur() function :

```python
dst = cv.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType=BORDER_DEFAULT]]] )
```

#### Parameters:

1. src	: input image
2. dst	: output image
3. ksize	: Gaussian Kernel Size. [height width]. height and width should be odd and can have different values. If ksize is set to [0 0], then ksize is computed from sigma values.
4. sigmaX :	Kernel standard deviation along X-axis (horizontal direction).
5. sigmaY	: Kernel standard deviation along Y-axis (vertical direction). If sigmaY=0, then sigmaX value is taken for sigmaY
6. borderType :	Specifies image boundaries while kernel is applied on image borders. Possible values are : cv.BORDER_CONSTANT cv.BORDER_REPLICATE cv.BORDER_REFLECT cv.BORDER_WRAP cv.BORDER_REFLECT_101 cv.BORDER_TRANSPARENT cv.BORDER_REFLECT101 cv.BORDER_DEFAULT cv.BORDER_ISOLATED

### Example – OpenCV Python Gaussian Blur:

```python
import cv2
import numpy
# read image
src = cv2.imread('../resources/python.png', cv2.IMREAD_UNCHANGED)
 
# apply guassian blur on src image
dst = cv2.GaussianBlur(src,(5,5),cv2.BORDER_DEFAULT)
 
# display input and output image
cv2.imshow("Gaussian Smoothing",numpy.hstack((src, dst)))
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

```

Note: Kernel size would be better to keep odd numbers 3,5,7, .. to get the better result