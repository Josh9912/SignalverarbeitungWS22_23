"""
Created on Fri Oct 02 00:22:52 2015

@author: Anton Winschel, Dan Zecha

This file constitutes a very basic introduction to Python programming and image manipulation.
Have a look at the examples and try to understand the concepts. Feel free to experiment
with the code. This will mostly be your tools for the homework assignments.

You will find more thorough explanations concerning Python on the online reference manual:
https://docs.python.org/3.6/reference/

For details on OpenCV there is an online documentation
https://docs.opencv.org/3.4.3/index.html


"""

# import libraries
import numpy as np                          # mathematical functions on arrays
import cv2 as cv                            # image processing

################################################################################
# TUTORIAL 1 (loading and saving images, pixel access and manipulation)

""" Reading an image can easily be done with the cv.imread function from the OpenCV
package which takes only the path to the image. You should always check if the
image was loaded correctly. """

img = cv.imread("Lenna.png")                # load image (datatype = numpy array)
assert(img is not None)                     # check if image was correctly loaded

""" An image has a height and width and either three channels (red, green and blue
-> color image) or one channel (greyscale image). You can retrieve all three as
follows. """

print("Image dimensions: " + str(img.shape)) # str() converts a number to a string
h,w,c = img.shape                           # retrieve height, width, number channels

""" Creates an empty color image filled with zeros, with 3 channels and uint8 precision.
Therefore, each pixel is represented by three 8-bit channels, i.e. the values range from
0 (black) to 255 (white). The image "flip" is initialized with zero values. """

flip = np.zeros((h,w,c), np.uint8)          # create an empty image filled with zeros

""" There are multiple ways of accessing pixel values. Note that the origin of an
image in OpenCV-Python is always the top-left corner of the image. Note also that
in Python, we always access the height variable first (this may be different
in other frameworks and programming languages, e.g. in C++).
We set the pixel at position x = 20 and y = 10 to white by setting all channels
to 255 like this (access order: img[y][x][c]):"""

img[10][20][0] = 255                        # blue channel
img[10][20][1] = 255                        # green channel
img[10][20][2] = 255                        # red channel

# if we wish to set or copy all channels of a pixel at the same time, we can also
# use the following. This is also very python-specific.

img[20][20] = 255

""" We will now copy each pixel from the original image to a second one and flip
all pixels during the procedure. While doing this, we will search for the smallest
value that a red pixel takes in our example image. """

# iterate over all pixels and flip image
smallest_red_value = 255                    # 255 is the highest value a pixel have

# xrange(h) = [0,1,...,h-1] -> we loop over the height of the image with y indices
for y in range(h):
    # same for the width
    for x in range(w):
        flip[y][x] = img[y][w-x-1]            # flip image at vertical axis
        if img[y][x][2] < smallest_red_value: # find minimal red value
            smallest_red_value = img[y][x][2]

print("The smallest red value in your image is : " + str(smallest_red_value))

""" Last but not least we want to show the images and hold them open as long as
the user does not press a key. After that, we close all windows (this is very
important as the python interpreter does not cope well with unclosed window handles."""

cv.imshow("img", img)                       # display image
cv.imshow("flipped", flip)                  # display flipped image
cv.waitKey()                                # wait for key press
cv.destroyAllWindows()                      # clean up, VERY IMPORTANT!

cv.imwrite("flipped.png", flip)             # save the flipped image to disk

""" With these simple functions you can write your own image processing functions.
For this simple example, the numpy library also has a function that flips a
matrix (and therefore also an image, as images are matrices): """

print("Smallest value numpy found: " + str(np.min(img[:,:,2])))
cv.imwrite("flipped_numpy.png", np.fliplr(img))


################################################################################
# TUTORIAL 2 (image manipulation)

""" OpenCV offers a wide range of image manipulation functions, for example for
resizing or drawing in images. There is also a lot of high level functionallity,
e.g. for computing image features, machine learning algorithms, image stitching,
etc. You can familiarise yourself with the OpenCV library here:
http://docs.opencv.org/modules/refman.html """

res = cv.resize(img, (200,200))             # resize image
cv.circle(res, (50,50), 25, (255,0,0), -1)  # draw blue circle at point=(50,50) with radius=25
cv.imwrite("circle.png", res)               # save image


################################################################################
# TUTORIAL 3 (complex numbers)

""" We will use complex numbers in this lecture. Numpy offers a class for complex
numbers which makes them very simple to use. """
c = np.complex(real=1, imag=4)              # define a complex number c = 1 + 4i
while(np.abs(c) < 10000):                   # as long as the absolute value is small
    print ("The absolute value of c = " + str(c) + " is " + str(np.abs(c)))
    c = c**2                                # square operation, i.e. c = c^2 = c*c
print("The absolute value of c = " + str(c) + " is " + str(np.abs(c)))


################################################################################
# TUTORIAL 4 (functions)

""" We also give you a bit of an introduction to handling functions in python",
as  """

# linear mapping
# map [a, b] -> [A, B]
# with f(x) = m*x + t
def lin_map(x, a, b, A, B):                 # define linear mapping function
    return (x-a)*(B-A)/(b-a) + A

h,w = 300,600                               # define new dimensions
gray = np.empty((h,w), np.float64)          # create empty double precision grayscale image

for y in range(h):
    for x in range(w):
        gray[y][x] = np.cos(0.05 * x)       # draw some cosine with regards to the columns

min_,max_ = np.min(gray), np.max(gray)      # find min and max values

# normalize values [min_,max_] -> [0,255] (linear mapping)
for y in range(h):
    for x in range(w):
        gray[y][x] = lin_map(gray[y][x], min_, max_, 0.0, 255.0)

# shorter opencv solution
gray_2 = np.empty((h,w), np.float64)
cv.normalize(gray, gray_2, 0.0, 255.0, cv.NORM_MINMAX)

gray = gray.astype(np.uint8)                # convert to uint8
gray_2 = gray_2.astype(np.uint8)
cv.imwrite("cosine.png", gray)              # save images
cv.imwrite("cosine_opencv.png", gray_2)

print("end of the brief Python tutorial :(")
