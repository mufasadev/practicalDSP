import numpy as np
from skimage.io import imread, imshow, show
from proc_func import procImageUsingKernel

kernel_blur = np.array([[1., 1., 1.],
                        [1., 1., 1.],
                        [1., 1., 1.]]) / 9.

n = int(input('matrix size (an odd number): '))
matrix = np.array([[1.] * n] * n) / (n * n)
print matrix
img = imread('images/pathtoimage')

imshow(img)
show()
imshow(procImageUsingKernel(img, matrix))
show()
