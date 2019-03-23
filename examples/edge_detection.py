import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

# read the image
image = mpimg.imread('../resources/exit-ramp.jpg')
plt.imshow(image)

# convert image to grayscale.
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
plt.imshow(gray, cmap='gray')

# gaussioan blur of the image with the kernel size
kernel_size = 11
gausssianBlur = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

# different methods for image detection
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)

laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=5)

canny = cv2.Canny(image, 100, 150)

# showing the image
plt.imshow(gausssianBlur, cmap='Greys_r')
plt.imshow(sobelx, cmap='Greys_r')
plt.imshow(sobely, cmap='Greys_r')
plt.imshow(laplacian, cmap='Greys_r')
plt.imshow(canny, cmap='Greys_r')

plt.show()