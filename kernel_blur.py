import numpy as np
import filters
from skimage.io import imread, imshow, show
from proc_func import procImageUsingKernel
from skimage.color import rgb2gray
from median_proc import median
import cv2

kernel_blur = np.array([[1., 1., 1.],
                        [1., 1., 1.],
                        [1., 1., 1.]]) / 9.

kernel_sharpen1 = np.array([[-1., -1., -1.],
                            [-1., 17., -1.],
                            [-1., -1., -1.]]) / 9.

kernel_sharpen2 = np.array([[0., -1., 0.],
                            [-1., 5., -1.],
                            [0., -1., 0.]])

kernel_edge_detect1 = np.array([[-1., -1., -1.],
                                [-1., 8., -1.],
                                [-1., -1., -1.]])

kernel_edge_detect2 = np.array([[0., -1., 0.],
                                [-1., 4., -1.],
                                [0., -1., 0.]])

kernel_stamping1 = np.array([[0, -1, 0],
                             [1, 0, -1],
                             [0, 1, 0]])

kernel_stamping2 = np.array([[0, 1, 0],
                             [-1, 0, 1],
                             [0, -1, 0]])
kernel_stamping_test = np.array([
    [0, -1, 0],
    [0, -1, 0],
    [1, -1, -1],
    [1, -1, -1],
    [1, 0, -1],
    [1, 1, -1],
    [1, 1, -1],
    [0, 1, 0],
    [0, 1, 0]]) * -1

no_result = np.array([[0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 0]])
no_result_1 = np.array([[1., 1., 1., 1.],
                        [1., 1., 1., 1.],
                        [1., 1., 1., 1.],
                        [1., 1., 1., 1.]]) / 12

kernel_gaussian = np.array([[1, 4, 6, 4, 1],
                            [4, 16, 24, 16, 4],
                            [6, 24, 36, 24, 6],
                            [4, 16, 24, 16, 4],
                            [1, 4, 6, 4, 1]]) / 256.

# n = int(input('matrix size (an odd number): '))
# matrix = np.array([[1.] * n] * n) / (n * n)
# print matrix
img = imread('images/a_h_1.png')

imshow(img)
show()
#

# imshow(procImageUsingKernel(img, matrix))
# show()
# imshow(cv2.filter2D(img, -1, no_result_1))
# show()
#
# imshow(procImageUsingKernel(img, kernel_blur))
# show()
#
# imshow(procImageUsingKernel(img, no_result))
# show()
#
# imshow(procImageUsingKernel(img, kernel_sharpen1))
# show()
# #
# imshow(procImageUsingKernel(img, kernel_sharpen2))
# show()
#
# imshow(procImageUsingKernel(img, kernel_edge_detect1))
# show()
#
# imshow(procImageUsingKernel(img, kernel_edge_detect2))
# show()

# imshow(procImageUsingKernel(rgb2gray(img), kernel_stamping1, 127))
# show()
#
# imshow(procImageUsingKernel(rgb2gray(img), kernel_stamping2, 127))
# show()
#
# imshow(procImageUsingKernel(rgb2gray(img), kernel_stamping_test, 127))
# show()

# watercolor
# imshow(procImageUsingKernel(median(rgb2gray(img)), kernel_sharpen1))
# show()

# imshow(procImageUsingKernel(img, kernel_gaussian))
# show()

# imshow(procImageUsingKernel(rgb2gray(img), filters.filter1()))
# show()

# imshow(procImageUsingKernel(rgb2gray(img), filters.filter2()))
# show()
#
# imshow(median(rgb2gray(img)))
# show()
